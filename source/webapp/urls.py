from django.urls import path

from source.webapp.views import index_view

urlpatterns = [
    path('', index_view),
]
