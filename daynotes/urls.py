from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    path('create/', views.create_note, name='create_note'),
    path('edit/<int:pk>/', views.edit_note, name='edit_note'),
    path('delete/<int:pk>/', views.delete_note, name='delete_note'),
]