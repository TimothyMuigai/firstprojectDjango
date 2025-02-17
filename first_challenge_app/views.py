from django.shortcuts import render
from .models import Blog
# Create your views here.

def home(request):
    context = {'msg':'Welcome!'}
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def display_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html',{'blogs': blogs})