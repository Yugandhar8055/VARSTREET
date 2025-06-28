from django.urls import path
from . import views

urlpatterns = [
    path('advanced-filter/', views.advanced_filter_from_text, name='advanced-filter-from-text'),
]
