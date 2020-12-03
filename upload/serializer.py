from rest_framework import serializers 

from .models import PhotoList,DocumentList

class PhotoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhotoList
        fields  = ["photo"]

class DocumentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentList
        fields  = ["document"]
