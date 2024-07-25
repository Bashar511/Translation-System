from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
# db for project
class Project(models.Model):
        title=models.CharField(max_length=50)
        owner = models.ForeignKey(User, related_name='owned_projects', on_delete=models.CASCADE)
        publish = models.DateTimeField(default=timezone.now)
        deliverytime=models.DateField()
        fileAR=models.FileField(upload_to='input',null=True)
        fileEN=models.FileField(upload_to='input')
        updated_dt = models.DateTimeField(null=True)

        class Meta:
            ordering = ['-publish']
            indexes = [
                models.Index(fields=['-publish']),
            ]
        def __str__(self):
            return self.title



class ProjectMember(models.Model):
    granted_to = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

