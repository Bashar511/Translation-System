from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.



class project1(models.Model):
        title=models.CharField(max_length=50)
        author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
        publish = models.DateTimeField(default=timezone.now)
        deliverytime=models.DateField()
        fileEN=models.FileField(upload_to='input')
        # updated_by = models.ForeignKey(User,null=True,related_name='+',on_delete=models.CASCADE)
        updated_dt = models.DateTimeField(null=True)

        class Meta:
            ordering = ['-publish']
            indexes = [
                models.Index(fields=['-publish']),
            ]
        def __str__(self):
            return self.title



class output_AI (models.Model):
        title=models.ForeignKey(project1,related_name='output',on_delete=models.CASCADE)
        fileAR=models.FileField(upload_to='out_ai')
        def __str__(self):
            return  self.title.title +" "



class processed_output_AI (models.Model):
    class Status(models.TextChoices):
        correct = 'ct', 'correct translation'
        not_verified_yet = 'ny', 'not verified yet'
        re_translated = 'rt', 're-translated'
    rfk=models.ForeignKey(output_AI,related_name='output',on_delete=models.CASCADE)
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
            title=str(self.starttime )
            return title 
        



