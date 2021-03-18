from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import ListView
# Create your models here.
class userFile(models.Model):
    title = models.CharField(max_length=150, blank=False)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    uploadDate = models.DateTimeField(default=timezone.now())
    realFile = models.FileField(upload_to='files/')
    YES = 'Yes'
    NO = 'No'
    FILE_OPTIONS = (
        ('Text','Text'),
        ('Image','Image'),
        ('Video','Video'),
        ('Audio','Audio'),
    )
    ALLOW_OTHERS = (
        (YES,'Allow'),
        (NO, 'Disallow')
    )

    permissionToDownload = models.CharField(
        max_length=3,
        choices=ALLOW_OTHERS,
        default=YES,
    )
    permissionToSeeUser = models.CharField(
        max_length=3,
        choices=ALLOW_OTHERS,
        default=YES,
    )
    FileType = models.CharField(
        max_length=5,
        choices=FILE_OPTIONS,
        default='Random'
    )

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.realFile.delete()
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('file-detail', kwargs={'pk': self.pk})
# class comment(models.Model):
#     post = models.ForeignKey()
#     user = models.ForeignKey(User,on_delete=models.CASCADE(), editable=False)
#     body = models.TextField(max_length=100, blank=False)
#     commentDate = models.DateTimeField(default=timezone.now())
#
#     class Meta:
#         ordering = ['created_on']
#
#     def __str__(self):
#         return 'New comment by {}'.format(self.user)



# Profile page area

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='users/default.jpg',upload_to='users')

    def __str__(self):
        return f'{self.user.username} Profile'; 