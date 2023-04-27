from django.conf import settings
from django.contrib.auth import authenticate, login as auth_login
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import CustomUserCreationForm, Thoughts


# Create your views here.
def about_me(request):
    """ Renders the about.html page when accessed on site

        :return: Returns about.html
    """
    return render(request, 'about.html')


#Define joing use, register function
def join_us(request):
    """ This function is for new users wanting to sign up

        :param form: Creates new user
        :param form.save: saves new user to database
        :param form.is_valid: Checks for user validation

        :return: Returns html to thank user for registering, or returns register.html for re-registration
        :rtype: HttpResponse

    """
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
    """ This function renders the contact page when accessed on the site

        :return: Returns contact page html for user to look at
        :rtype: HttpResponse
    """
    return render(request, 'contact.html')


# Recall home page
def home_page(request):
    """ This function renders the home page, first page when on the site

        :return: Returns home page html for user to look at
        :rtype: HttpResponse
    """
    return render(request, 'home.html')


# When adding thoughts, if user is logged in they can be allowed to like and comment
def thoughts(request):
    """ This function renders the thought page, cantaining all the hought-posts added by admin

        :param thoughts: Returns thoughts in chronological order
        :param if.request.user.is_authenticated: Checks if user is logged in before being able to access the page 

        :return: thoughts.html if user is authenticated, otherwise not_logged_in.html if usern isn't
        :rtype: HttpResponse
    """
    if request.user.is_authenticated:
        thoughts = Thoughts.objects.all().order_by('created_at')
        return render(request, 'thoughts.html', {'thoughts': thoughts})

    else:
        return render(request, 'not_logged_in.html')

def login(request):
    """ This function provides users with the option to log in, in order to access more on the site 

        :param request: HttpResponse object returning request
        :type request: HttpRequest

        :return: if user is logged in, redirects to about.html. If wrong input, login.html is reloaded. else. user is directed to login.html
        :rtype: HttpResponse
    """
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
    """ This function renders the logged_in.html, if user login was successfull

        :param request: Httprequest object, representing current request
        :type request: HttpRequest

        :return: Returns logged_in.html page if user is successfully logged in
        :rtype: HttpResponse
    """
    username = request.user.username
    return render(request, 'logged_in.html', {'username': username})

