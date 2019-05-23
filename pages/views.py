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
    form = ProductForm(request.POST or None)
    if form.is_valid():
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
    else:
        print(form.errors)
    context = { 
        "title": "Shorten your link here",
        "form" : form,
    }
    return render(request, "home.html", context)

def home_red(request):
    return redirect('/home')

class UserPostListView(ListView):
    model = Product
    template_name = 'user_posts.html'
    context_object_name = 'links'

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Product.objects.filter(author=user).order_by('-date_posted')

def dynamic_lookup_view(request, rd):
    if isinstance(rd,str):
        return redirect(rd)
    m_id = decode(rd)
    obj = get_object_or_404(Product,id=m_id)
    print("Red link %s"%str(obj.link))

    return redirect(obj.link)
