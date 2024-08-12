from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
import os

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

        def clean(self):
                super().clean()
                if self.fileEN:
                    ext = os.path.splitext(self.fileEN.name)[1].lower()
                    if ext != '.srt':
                        raise ValidationError({'fileEN': _('فقط ملفات .srt مسموح بها.')})

        def save(self, *args, **kwargs):
                self.clean()
                super().save(*args, **kwargs)

class ProjectMember(models.Model):
    granted_to = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
