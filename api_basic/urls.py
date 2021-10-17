from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import ArticleAPIView, ArticleDetails, article_details, article_list, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')


urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('func/articles/', article_list),
    path('func/article/<int:pk>/', article_details),
    path('class/articles/', ArticleAPIView.as_view()),
    path('class/article/<int:id>/', ArticleDetails.as_view()),
    path('generic/articles/<int:id>/', GenericAPIView.as_view()),
    path('generic/articles/', GenericAPIView.as_view())
]
