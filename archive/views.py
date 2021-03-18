
from django.shortcuts import render
from users.models import userFile
# Create your view of the pages here.

def homepage(request):
    files = userFile.objects.all()
    return render(request, 'archive/home.html', {
        'posts': files
    })

def aboutUs(request):
    return render(request, 'archive/about.html', {'title':'About'})

