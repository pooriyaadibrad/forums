from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def blog(request):
    return render(request, 'blog.html',context={})
def contact(request):
    return render(request=request,template_name='Contact_us.html')