
from django.urls import path
from news.views import index, catalog, partner

urlpatterns = [
    path ('', index),
    path ('catalog', catalog),
    path ('partner', partner),
]
