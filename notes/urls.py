from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.NoteListView.as_view(), name='note-list'),
    path('notes/note/create/', views.NoteCreateView.as_view(), name='note-create'),
    path('notes/note/update/<int:pk>/', views.NoteUpdateView.as_view(), name='note-update'),
    path('notes/note/delete/<int:pk>/', views.NoteDeleteView.as_view(), name='note-delete'),
]