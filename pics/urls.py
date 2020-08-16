from . import views
from django.urls import path

urlpatterns = [
	path('delete_screenshot/<str:name>', views.delete_screenshot, name='delete_screenshot'),
    path('', views.home, name='pics')
]
