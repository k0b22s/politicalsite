from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms


# Create your models here.
class Thoughts(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

