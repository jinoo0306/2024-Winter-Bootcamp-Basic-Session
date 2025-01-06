from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from .models import Poster
from .serializers import PosterSerializer
from datetime import datetime

class mainPosterView(APIView):
    @swagger_auto_schema(request_body=PosterSerializer,
                         responses={201: PosterSerializer})
    def post(self, request, *args, **kwargs):
        serializer = PosterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        posts = Poster.objects.filter(deleted_at__isnull=True)  # 삭제되지 않은 게시물만 필터링
        serializer = PosterSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PosterView(APIView):
    def get(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        if post_id:
            post = Poster.objects.filter(id=post_id, deleted_at__isnull=True).first()
            if post:
                serializer = PosterSerializer(post)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        posts = Poster.objects.filter(deleted_at__isnull=True)
        serializer = PosterSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=PosterSerializer,  # 요청 본문에 사용할 Serializer
        operation_description="Update a poster"
    )
    def put(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        post = Poster.objects.filter(id=post_id, deleted_at__isnull=True).first()
        if not post:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PosterSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        post = Poster.objects.filter(id=post_id, deleted_at__isnull=True).first()
        if not post:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        # 현재 시간을 deleted_at에 저장
        post.deleted_at = datetime.now()
        post.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


