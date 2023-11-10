from django.urls import path
from .views import boot, output, download,login

urlpatterns = [
    path('', boot, name='boot'),
    path('output/<str:csv_file_name>/', output, name='output'),
    path('download/<str:csv_file_name>/', download, name='download'),
    path('login/',login, name='login'),
]
