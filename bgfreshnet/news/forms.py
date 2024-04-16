
from django import forms
from bgfreshnet.news.models import Article

class ArticleBaseForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'article_image']

        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Заглавие на статия", "size": 50}),
            "content": forms.Textarea(attrs={"placeholder": "Съдържание", "rows": 10, "cols": 60}),
            "article_image": forms.URLInput(attrs={"placeholder": "Връзка към изображение"}),
        }
        labels = {
            "title": "Заглавие",
            "article_image": "Link to image",
            "content": "Съдържание",
        }

class ArticleCreateForm(ArticleBaseForm):
    pass