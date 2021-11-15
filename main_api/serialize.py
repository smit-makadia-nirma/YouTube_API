from rest_framework import serializers
from .models import Video


# Serializers to allow querysets and model instances converted to native Python datatypes to be rendered as JSON or XML.
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"
