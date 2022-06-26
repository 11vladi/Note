from . import views
from django.urls import path

urlpatterns = [
     path('', views.index, name='index'),
     path('my-notes', views.notes, name='my-notes'),
     path('new', views.new_note, name='new-note'),
     path('rename', views.rename_note, name='rename-note'),
     path('delete', views.delete_notes, name='delete-notes'),
     path('text-loading', views.text_loading, name='text-loading'),
     path('text-save', views.text_save, name='text-save'),
]