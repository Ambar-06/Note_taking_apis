from django.urls import path
from application_apis import views

urlpatterns = [
    path('', views.NoteViews.as_view(), name='notes'),
    path('<int:note_id>/', views.SingleNoteView.as_view(), name='single_note'),
]
