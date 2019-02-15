from django.urls import path
from webapp import home
from . import views

app_name = 'home'
urlpatterns = [
    path('home/', views.home(), name='home'),
]