#forms.py 

from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    """
    ProductForm class inferits Django's ModelForm class
    has a single line that asks for a link
    """
    class Meta:
        model = Product
        fields = [
            "link",
        ]
    def clean_link(self):
        """
        clean_link(self,/)
        returns an exception to the page if link is not valid
        also adds a http(s):// to the link if it is not already in it
        also, without the http:// part heroku and django can 
        start an infinite loop or run your apps uproperly.
        """

        link = self.cleaned_data.get('link')
        if "." not in link:
            raise forms.ValidationError("This is not a valid url")
        if "http:" not in link and "https:" not in link:
            link = 'http://%s'%link 
        return link
