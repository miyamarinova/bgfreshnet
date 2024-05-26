from django import forms
from bgfreshnet.common.models import ProductComment

class ProductSearchForm(forms.Form):
    query = forms.CharField(label='Търси продукт', max_length=50)

class ProducerSearchForm(forms.Form):
    query = forms.CharField(label='Търси производител', max_length=50)

class ContactForm(forms.Form):
    contact_name = forms.CharField(
        required=True,
        label="Name"
    )
    contact_email = forms.EmailField(
        required=True,
        label="Email"
    )
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="Message"
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Добави коментар...'})
        }