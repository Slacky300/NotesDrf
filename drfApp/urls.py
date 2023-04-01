
from django.urls import path, include
from . import views
from rest_framework import routers




urlpatterns = [
    
    path('notes/',views.NotesList.as_view()),
    path('notes/<int:pk>/',views.NoteDetail.as_view()),
    path('subjects/',views.SubjectList.as_view()),
    path('subjects/<int:pk>/',views.SubjectDetail.as_view()),
    path('comments/',views.CommentList.as_view()),
    path('comments/<int:pk>/',views.CommentDetail.as_view()),
    path('commentReply/',views.CommentReply.as_view()),
    path('commentReply/<int:pk>/',views.CommentReplyDetail.as_view()),
    


]