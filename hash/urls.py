from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delete/<int:pk>/', views.delete_word, name='delete_word'),
]
