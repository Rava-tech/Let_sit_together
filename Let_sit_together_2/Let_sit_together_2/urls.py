"""
URL configuration for Let_sit_together_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Lets_sit_together_4 import views
from django.contrib.auth.views import LoginView, LogoutView
from Lets_sit_together_4.views import register, search, welcome_view, logout_view, profile_view, \
    search_map, search_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('search/', search, name='search'),
    path('welcome/', welcome_view, name='welcome'),
    path('logout/', logout_view, name='logout'),
    path('accounts/profile/', profile_view, name='profile'),
    path('map/', search_map, name='map'),
    path('search_results/', search_view, name='search_results'),
]
