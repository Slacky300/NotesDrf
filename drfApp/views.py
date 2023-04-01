
from rest_framework import generics
from rest_framework import permissions

from . models import *
from . serializers import *




class NotesList(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [permissions.IsAuthenticated]


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [permissions.IsAuthenticated]

class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]

class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentReply(generics.ListCreateAPIView):
    queryset = CmntReply.objects.all()
    serializer_class = CmntReplySerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CmntReply.objects.all()
    serializer_class = CmntReplySerializer
    permission_classes = [permissions.IsAuthenticated]