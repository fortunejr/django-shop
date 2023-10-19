from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignUpForm
from django.contrib.auth import logout

# The function to handle the homepage.
def index(request):
    items = Item.objects.filter(is_sold=False) # Getting the all newest unsold products
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

# The function handling the contact page.
def contact(request):
    return render(request, 'core/contact.html',)
# When the users usccesfully signup, it redirects to the login page
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {
        'form': form
    })


def logoutuser(request):
    logout(request.user)
    return render(request, 'core/index.html')