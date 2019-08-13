from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from blog.views import CommonViewMixin
from .models import Link
# Create your views here.

class LinkListView(CommonViewMixin,ListView):
    '''友链'''
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
    template_name = 'config/links.html'
    context_object_name = 'link_list'



