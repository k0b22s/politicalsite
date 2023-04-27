from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "about"

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about_me/', views.about_me, name='about_me'),
    path('join_us/', views.join_us, name='join_us'),
    path('contact/', views.contact, name='contact'),
    path('thoughts/', views.thoughts, name='thoughts'),
    path('login/', views.login, name='login'),
    path('logged_in/', views.logged_in, name='logged_in'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)