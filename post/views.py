from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    posts = models.post.objects.all()
    return render(request, 'index.html',context={'posts':posts})
def blog(request):
    return render(request, 'blog.html',context={})
def contact(request):
    return render(request=request,template_name='Contact_us.html')