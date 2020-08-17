from . import views
from django.urls import path, re_path

urlpatterns = [
	path('delete_screenshot/', views.delete_screenshot, name='delete_screenshot'),
    path('', views.home, name='pics')
]
