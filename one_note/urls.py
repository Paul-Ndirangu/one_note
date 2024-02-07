from django.contrib import admin
from django.urls import path

from document.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('custom_logout_page/', custom_logout, name='logout'),
    path('', editor, name='editor'),
    path('delete_document/<int:docid>/', delete_document, name='delete'),
]
