from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from bgfreshnet.news.decorators import admin_group_required
from bgfreshnet.news.forms import ArticleCreateForm
from bgfreshnet.news.models import Article

# Create your views here.

class AllArticlesView(views.ListView):
    model = Article
    template_name = 'news/all-articles.html'
    context_object_name = 'articles'

@method_decorator(admin_group_required, name='dispatch')
class AddArticleView(views.CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'news/add-article.html'
    success_url = reverse_lazy('all articles')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DetailArticleView(views.DetailView):
    model = Article
    template_name = 'news/detail-article.html'
    context_object_name = 'article'