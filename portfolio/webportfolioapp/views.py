from django.shortcuts import render
from .forms import ContactForm
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'webportfolioapp/blog.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'webportfolioapp/blog_detail.html', {'blog': blog})

def home(request):
    return render(request, 'webportfolioapp/home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    return render(request, 'webportfolioapp/contact.html', {'form': form})