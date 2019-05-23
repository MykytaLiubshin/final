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
        if "." not in link:
            raise forms.ValidationError("This is not a valid url")
        return link
