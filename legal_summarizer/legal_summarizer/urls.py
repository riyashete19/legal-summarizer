from django.urls import path
from django.http import HttpResponse  # Add this for the home page response
from summarizer.views import summarize_document

urlpatterns = [
    path('', lambda request: HttpResponse("Welcome to the Legal Summarizer API!")),
    path('api/summarize/', summarize_document, name='summarize_document'),
]
