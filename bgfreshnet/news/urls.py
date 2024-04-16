from django.urls import path
from bgfreshnet.news.views import (AllArticlesView, AddArticleView, DetailArticleView,
                                   EditArticleView, DeleteArticleView)


urlpatterns = [
    path('all-articles/',AllArticlesView.as_view(), name='all articles'),
    path('add-article', AddArticleView.as_view(), name='add article'),
    path('<int:pk>/', DetailArticleView.as_view(), name='detail article'),
    path('<int:pk>/edit/', EditArticleView.as_view(), name='edit article'),
    path('<int:pk>/delete/', DeleteArticleView.as_view(), name='delete article')
]