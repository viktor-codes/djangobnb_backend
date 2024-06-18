from django.urls from django.urls import path

from . import api

urlpatterns = [
    path('conversations/', api.conversations_list, name="api_conversations_list"),
]