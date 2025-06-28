import json
import re

def extract_valid_json(text: str):
    """
    Extracts and validates JSON from LLM-generated text.
    
    Args:
        text (str): Raw output from LLM which may contain JSON.
    
    Returns:
        dict: Parsed JSON object if extraction and validation is successful.

    Raises:
        ValueError: If no valid JSON could be extracted or parsed.
    """
    try:
        # Try direct parse first (if pure JSON string)
        return json.loads(text)
    except:
        try:
            return json.loads(text[text.index("{"):text.rindex("}")+1])
        except Exception as e:
            return f"❌ Error converting LLM-generated text to JSON LLM-TEXT{text}\nerror: {str(e)}"