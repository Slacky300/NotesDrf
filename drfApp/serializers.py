from . models import *
from rest_framework import serializers

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        # exclude = ['slug']
        fields = '__all__'
        

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        

class CmntReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = CmntReply
        fields = '__all__'