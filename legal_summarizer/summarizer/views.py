from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .ml_model import summarizer
import json

@csrf_exempt
def summarize_document(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text', '')
            if not text:
                return JsonResponse({'error': 'No text provided'}, status=400)
            
            summary = summarizer.summarize(text)
            return JsonResponse({'summary': summary})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
