# Generated by Django 3.2.25 on 2024-08-12 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translationSite', '0002_alter_project_fileen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='fileEN',
            field=models.FileField(upload_to='input'),
        ),
    ]
