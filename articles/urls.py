"""kxjblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

from articles.views import IndexView, ArticlesDetailView, ArticlesListView, Index1View, ArticlesSearchView
from user.models import User
app_name = 'articles'
urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('index1/', Index1View.as_view(), name='index1'),
    path('detail/<str:articles_id>', ArticlesDetailView.as_view(), name='detail'),
    path('detail1/<str:sort_id>', ArticlesListView.as_view(), name='list'),
    path('search/', ArticlesSearchView.as_view(), name='search'),
]
