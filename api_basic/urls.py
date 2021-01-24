from django.urls import path
from django.urls.conf import include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
	path('viewset/', include(router.urls)),
	#path('article/', article_list),
	path('article/', ArticleApiView.as_view()),
	#path('detail/<int:pk>/', article_detail),
	path('detail/<int:id>/', ArticleDetailApiView.as_view()),
	path('generic/article/', GenericApiView.as_view()),
	path('generic/article/<int:id>', GenericApiView.as_view()),
]
