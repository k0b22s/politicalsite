from django.conf import settings
from django.contrib.auth import authenticate, login as auth_login
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import CustomUserCreationForm, Thoughts


# Create your views here.
def about_me(request):
    return render(request, 'about.html')


#Define joing use, register function
def join_us(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank_you.html')

    else:
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})


#Return contact page, static
def contact(request):
    return render(request, 'contact.html')


# Recall home page
def home_page(request):
    return render(request, 'home.html')


# When adding thoughts, if user is logged in they can be allowed to like and comment
def thoughts(request):
    if request.user.is_authenticated:
        thoughts = Thoughts.objects.all().order_by('created_at')
        return render(request, 'thoughts.html', {'thoughts': thoughts})

    else:
        return render(request, 'not_logged_in.html')

def login(request):
    #prompt user with login features
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # check for authentication, before allowing user to login
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('about:logged_in')

        #i.c.e. wrong login credentials
        else:
            error = 'You seem to have entered the wrong username or password. Please try again'
            return render(request, 'login.html', {'error': error})

    else:
        return render(request, 'login.html')


#for when user is logged in, to welcome them back
def logged_in(request):
    username = request.user.username
    return render(request, 'logged_in.html', {'username': username})

