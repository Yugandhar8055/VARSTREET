from django.urls import path
from . import views

urlpatterns = [
    path('advancedAIFilter/', views.advanced_filter_from_text),
]
