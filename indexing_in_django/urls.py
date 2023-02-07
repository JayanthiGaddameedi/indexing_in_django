from django.contrib import admin
from django.urls import path

from datarepo.views import create_data, get_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_data/', create_data),
    path('get_data/', get_data),
]
