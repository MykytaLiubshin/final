from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from pages.views import homepage_view, home_red, dynamic_lookup_view, UserPostListView
from users.views import register_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_red),
    path('home/', homepage_view),

    path("register/", register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name = 'users/login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name="logout"),
    
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),

    path(r'home/'+('<str:rd>'), dynamic_lookup_view, name = 'result')
]

