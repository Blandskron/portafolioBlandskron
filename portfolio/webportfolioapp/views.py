from django.shortcuts import render
from .forms import ContactForm

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