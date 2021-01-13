from django.urls import path
from .views import article_list, article_detail, ArticleApiView, ArticleDetailApiView


urlpatterns = [
	#path('article/', article_list),
	path('article/', ArticleApiView.as_view()),
	#path('detail/<int:pk>/', article_detail),
	path('detail/<int:id>/', ArticleDetailApiView.as_view()),
]
