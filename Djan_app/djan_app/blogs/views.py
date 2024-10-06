from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Blog

# Create your views here.
def blogs(request):
    blogs = Blog.objects.all().values()
    context = {'blogs': blogs}

    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))
