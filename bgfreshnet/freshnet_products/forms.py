from django import forms

from bgfreshnet.freshnet_products.models import FreshNetProduct


class ProductBaseForm(forms.ModelForm):
    class Meta:
        model = FreshNetProduct
        fields = ['name', 'description', 'price', 'product_image']

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Product name"}),
            "description": forms.DateInput(attrs={"placeholder": "Description of the product"}),
            "product_image": forms.URLInput(attrs={"placeholder": "Link to image"}),
        }

        labels = {
            "name": "Product name",
            "product_image": "Link to image",
        }

class ProductCreateForm(ProductBaseForm):
    pass


