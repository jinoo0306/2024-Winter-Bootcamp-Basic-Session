from rest_framework import serializers
from .models import Poster

class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'deleted_at']
        read_only_fields = ['id','created_at', 'updated_at', 'deleted_at']  # 읽기 전용 필드 설정

