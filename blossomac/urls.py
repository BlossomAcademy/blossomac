"""blossomac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from datascience import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='index'),
    url(r'^fasttrack/', views.join_blossom, name='fasttrack'),
    url(r'^immersive/', views.become_partner, name='immersive'),
    url(r'^about/', views.about_us, name='about'),
    url(r'^privacypolicy/', views.privacy_policy, name='privacypolicy'),
    url(r'^terms/', views.terms_services, name='terms'),
    url(r'^faqs/', views.faqs, name='faqs')
]
 