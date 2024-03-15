from django.shortcuts import render
from django.views import generic as views
# Create your views here.

class IndexView(views.TemplateView):
    template_name = 'common/index.html'
