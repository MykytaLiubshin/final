from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Product
from .forms import ProductForm
from .coder import coding, decode

def homepage_view(request):
    """
    The homepage view that shows you the form for a link
    returns a rendered homepage, where you can make a link
    than returns an output of making_link function
    """
    form = ProductForm(request.POST or None)
    if form.is_valid():
          return making_link(request)
    else:
        print(form.errors)
    context = { 
        "title": "Shorten your link here",
        "form" : form,
    }
    return render(request, "home.html", context)

def making_link(request):
    """
    making_link(request,/)
    returns a result page w/ your shorten link
    """

    obj = form.save(commit=False)
    if isinstance(request.user,User):
        obj.author = request.user
    form.save()
    a = form.save()
    print(a)
    form = ProductForm()
    standard_domain = "https://linksho.herokuapp.com/home/"
    context = {
        'std' : standard_domain,
        'link' : coding(a.id),
    }
    return render(request, 'result.html',context)

def home_red(request):
    """
    home_red(request,/)
    Redirects you from the app link to the home link
    """
    return redirect('/home')

class UserPostListView(ListView):
    """
    UserPostListView(ListView) inherits from django's ListView
    returns a list of liks created by someone sorted by the time it was added 
    """
    model = Product
    template_name = 'user_posts.html'
    context_object_name = 'links'

    def get_queryset(self):
        """
        get_queryset(self,/) 
        returns a queryset of all the links created by a specific user
        """
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Product.objects.filter(author=user).order_by('-date_posted')

def dynamic_lookup_view(request, rd):
    """
    dynamic_lookup_view(request, rd,/)
    returns a redirect to a needed link
    """
    m_id = decode(rd)
    obj = get_object_or_404(Product,id=m_id)

    return redirect(obj.link)
