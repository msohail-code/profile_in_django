"""galleria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from users.views import fileDetail, createFile, updateFile, deleteFile
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('archive.urls')),
    path('register/',user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('file/<int:pk>/', fileDetail.as_view(),name='file-detail'),
    path('file/<int:pk>/update', updateFile.as_view(), name='update'),
    path('file/<int:pk>/delete', deleteFile.as_view(), name='delete'),
    #path('class/files/', user_views.ShowFileView.as_view(), name='class_file'),
    #path('class/files/<int:pk>/',user_views.delete_file, name='delete_file'),
    path('profile/files/', user_views.show_files, name='files'),
    #path('profile/upload/', user_views.upload_file, name='upload')
    path('profile/upload/', createFile.as_view(), name='upload')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)