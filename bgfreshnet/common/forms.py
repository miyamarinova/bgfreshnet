from django import forms
from bgfreshnet.common.models import ProductComment

class ProductSearchForm(forms.Form):
    query = forms.CharField(label='Търси продукт', max_length=50)

class ProducerSearchForm(forms.Form):
    query = forms.CharField(label='Търси производител', max_length=50)

class ContactForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Твоят e-mail"})
    )
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Tema"}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Twoqeto syob]enie"})
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Добави коментар...'})
        }