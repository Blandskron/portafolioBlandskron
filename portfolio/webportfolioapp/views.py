from django.shortcuts import render, redirect
from .forms import ContactForm


def home(request):
    return render(request, 'webportfolioapp/home.html')

def softskills(request):
    return render(request, 'webportfolioapp/softskills.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_message')
    else:
        form = ContactForm()
    return render(request, 'webportfolioapp/contact.html', {'form': form})

def success_message(request):
    return render(request, 'webportfolioapp/success.html')
