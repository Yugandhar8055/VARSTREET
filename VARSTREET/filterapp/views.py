import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from llm_client import callAdvancedFilter

@csrf_exempt
@require_POST
def advanced_filter_from_text(request):
    """Simple filter API that extracts words containing 'advanced'."""
    
    data = json.loads(request.body)
    response = callAdvancedFilter(data.get("userQuery"),data.get("jsonID"))

    if type(response) == dict:
        return JsonResponse({'results': response,
                             'error':None
        })
    else:
        return JsonResponse({'results':None,
                             'error':response
        })
