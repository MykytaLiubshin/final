from django import forms


from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "link",
        ]
    def clean_link(self):
        link = self.cleaned_data.get('link')
        valid = True
        redirect = ""
        if "https" not in link:
            link = 'https://%s'%link
        return link
