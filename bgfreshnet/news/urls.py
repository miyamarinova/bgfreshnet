from django.urls import path
from bgfreshnet.news.views import AllArticlesView, AddArticleView, DetailArticleView

urlpatterns = [
    path('all-articles/',AllArticlesView.as_view(), name='all articles'),
    path('add-article', AddArticleView.as_view(), name='add article'),
    path('<int:pk>/', DetailArticleView.as_view(), name='detail article'),
]