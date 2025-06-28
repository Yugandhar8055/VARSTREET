import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST

@require_POST
def advanced_filter_from_text(request):
    """Simple filter API that extracts words containing 'advanced'."""
    try:
        payload = json.loads(request.body.decode())
        text = payload.get('text', '')
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON')

    filtered = [word for word in text.split() if 'advanced' in word.lower()]
    return JsonResponse({'filtered_words': filtered})
