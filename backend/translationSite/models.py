from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class project(models.Model):
        title=models.CharField(max_length=50)
        author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
        publish = models.DateTimeField(default=timezone.now)
        deliverytime=models.DateTimeField()
        fileEN=models.FileField()
        fileAR=models.FileField()
        
        class Meta:
            ordering = ['-publish']
            indexes = [
                models.Index(fields=['-publish']),
            ]
        def __str__(self):
            return self.title

class outputAI (models.Model):
    class Status(models.TextChoices):
        correct = 'ct', 'correct translation'
        not_verified_yet = 'ny', 'not verified yet'
        re_translated = 'rt', 're-translated'
    title=models.ForeignKey(project,related_name='output',on_delete=models.CASCADE)
    sentenceEN=models.TextField(max_length=1000)
    sentenceAR=models.TextField(max_length=1000)
    starttime=models.TimeField()
    endtime=models.TimeField()
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.not_verified_yet)
    
    class Meta:
            ordering = ['starttime']
            indexes = [
                models.Index(fields=['starttime']),
            ]
    
    def __str__(self):
        return self.title
    



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    
    def __str__(self):
        return f'Profile of {self.user.username}'
