from django.urls import path
from . import views
from users import views as user_views


urlpatterns = [
    path('', views.homepage, name='archive-home'),
    path('about/', views.aboutUs, name='archive-about'),
    path('register/', user_views.register, name='user-register')
]
