"""list_of_lists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from lister.views import view_lists, view_list, add_new_list, add_new_thing

urlpatterns = [
    url(r'^$', view_lists),
    url(r'^/$', view_lists),
    url(r'^add/$', add_new_list),
    url(r'^(?P<list_slug>[a-z\-]+)$', view_list),
    url(r'^(?P<list_slug>[a-z\-]+)/add/$', add_new_thing),
    url(r'^admin/', include(admin.site.urls)),
]
