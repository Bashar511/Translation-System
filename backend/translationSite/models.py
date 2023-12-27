from django.db import models

# Create your models here.

class project(models.Model):
        nameproject=models.CharField(max_length=50)
        deliverytime=models.DateTimeField()
        fileEN=models.FileField()
        fileAR=models.FileField()


class outputAI (models.Model):
    nameproject=models.ForeignKey(project,related_name='output',on_delete=models.CASCADE)
    sentenceEN=models.TextField(max_length=1000)
    sentenceAR=models.TextField(max_length=1000)
    starttime=models.TimeField()
    endtime=models.TimeField()
    sentence_status = [
        ('correct translation','correct translation'),
        ('not verified yet','not verified yet'),
        ('re-translated','re-translated'),
        
    ]
    status=models.CharField(max_length=25,choices=sentence_status,default='not verified yet')




