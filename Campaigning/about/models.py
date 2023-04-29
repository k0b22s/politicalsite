from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms


# Create your models here.
class Thoughts(models.Model):
    """ This module is for the admin of the site to add his/her thoughts.
        These thoughts will then get published on the site.

        :param title: String representation of post-title
        :param body: String representation of post-body
        :param created-at: DateTime representation of when post was created

    """
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Returns a string representation fo the post

            :return: Returns string representation fo post
        """
        return self.title



class CustomUserCreationForm(UserCreationForm):
    """ This module is for the creation of new users, registering on the site.

        :param email: Provides that form can't validate without email field
    """
    email = forms.EmailField(required=True)

    class Meta:
        """
            :param model: Creates new user
            :param fields: Defines the input required to create a new user
        """
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        """ Save new user instance to database

            :param user.email: Email adress associated with new user
            :param commit: If True, new user is added to database

            :return: Saved user instance
        """
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

