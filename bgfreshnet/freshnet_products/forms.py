from django import forms
from .models import FreshNetProduct

class ProductBaseForm(forms.ModelForm):
    price = forms.DecimalField(max_digits=10, decimal_places=2,
                               label="Цена",
                               widget=forms.NumberInput(attrs={"placeholder": "Цена в лева"}))
    class Meta:
        model = FreshNetProduct
        fields = ['name', 'description', 'price', 'product_image']

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Име на продукта"}),
            "description": forms.TextInput(attrs={"placeholder": "Кратко описание", "size":50}),

        }

class ProductCreateForm(ProductBaseForm):
    pass

class ProductEditForm(ProductBaseForm):
    pass