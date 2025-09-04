from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from llm_client import callAdvancedFilter

# Initialize Flask app
app = Flask(__name__)

# Simple configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['DEBUG'] = os.environ.get('DEBUG', 'True').lower() == 'true'

# CORS configuration
cors_origins = os.environ.get('CORS_ALLOWED_ORIGINS', '*')
if cors_origins != '*':
    cors_origins = cors_origins.split(',')
else:
    cors_origins = ['*']

CORS(app, origins=cors_origins)

@app.route('/health/', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200

@app.route('/api/advancedAIFilter/', methods=['POST'])
def advanced_filter_from_text():
    """Advanced filter API endpoint"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        user_query = data.get("userQuery")
        screenURL = data.get("screenURL")
        
        if not user_query or not screenURL:
            return jsonify({'error': 'Missing userQuery or screenURL'}), 400
        
        response = callAdvancedFilter(user_query, screenURL)
        
        if isinstance(response, dict):
            return jsonify({
                'results': response,
                'error': None
            })
        else:
            return jsonify({
                'results': None,
                'error': response
            })
    
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/', methods=['GET'])
def index():
    """Root endpoint"""
    return jsonify({
        'message': 'VARSTREET Flask API',
        'version': '1.0.0',
        'endpoints': {
            'health': '/health/',
            'advanced_filter': '/api/advancedAIFilter/'
        }
    })

if __name__ == '__main__':
    # Development server
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG']) 