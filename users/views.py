from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm #framework libr for making user creation forms
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import fileForm, UserUpdateForm, ProfileUpdateForm
from .models import userFile
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required()
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'users/profile.html', context)

class fileDetail(DetailView):
    model = userFile
    template_name = "users/file.html"
    context_object_name = 'file'
    ordering = ['-uploadDate']

class createFile(CreateView, LoginRequiredMixin):
    model = userFile
    template_name = "users/upload_file.html"
    context_object_name = 'form'
    fields = ['title','realFile','permissionToDownload','permissionToSeeUser','FileType']

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)

class updateFile(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = userFile
    template_name = "users/upload_file.html"
    context_object_name = 'form'
    fields = ['title','realFile','permissionToDownload','permissionToSeeUser','FileType']

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)

    def test_func(self):
        file = self.get_object()
        if self.request.user == file.uploader:
            return True
        return False

class deleteFile(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = userFile
    template_name = "users/delete.html"
    success_url = '/profile/files/'

    def test_func(self):
        file = self.get_object()
        if self.request.user == file.uploader:
            return True
        return False
#####################################################
##Old versions  of file upload, view, and deletion
#
@login_required()
def show_files(request):
    files = userFile.objects.filter(uploader=request.user)
    return render(request, 'users/show_files.html',{
        'files': files
    })
#
# @login_required()
# def upload_file(request):
#
#     if request.method == 'POST':
#         form = fileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.instance.uploader = request.user
#             form.save()
#             return redirect('files')
#     else:
#         form = fileForm()
#     return render(request,'users/upload_file.html',{
#         'form':form
#     })
#
# @login_required()
# def delete_file(request, pk):
#     if request.method == 'POST':
#         file = userFile.objects.get(pk=pk)
#         if request.user == file.uploader:
#             file.delete()
#             messages.success(request, f'item deleted for {file.uploader}')
#
#     return redirect('files')
########################################################################







# class ShowFileView(ListView):
#     model = userFile
#     template_name = 'users/show_files.html'
#     context_object_name = 'files'

# @login_required()
# def add_comment(request, pk):
#     if request.method == 'POST':
#         form = commentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.instance.user = request.user
#             form.save()
#             return redirect('')
#     else:
#         form = fileForm()
#     return render(request, 'users/upload_file.html', {
#         'form': form
#     })



# Edit user area

@login_required()
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'users/edit-profile.html', context)
