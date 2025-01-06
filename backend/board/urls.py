from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path
from .views import PosterView
from .views import mainPosterView

schema_view = get_schema_view(
    openapi.Info(
        title="게시판 API",
        default_version='v1',
        description="게시판 API의 Swagger 문서",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Swagger UI 문서 페이지
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # 게시물 목록 조회 및 생성
    path('api/v1/boards', mainPosterView.as_view(), name='board-list-create'),
    # 특정 게시물 조회, 수정 및 삭제
    path('api/v1/boards/<int:id>', PosterView.as_view(), name='board-detail-update-delete'),
]
