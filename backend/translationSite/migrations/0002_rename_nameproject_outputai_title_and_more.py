# Generated by Django 5.0.1 on 2024-01-10 17:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translationSite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outputai',
            old_name='nameproject',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='nameproject',
            new_name='title',
        ),
        migrations.AddField(
            model_name='project',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='outputai',
            name='status',
            field=models.CharField(choices=[('ct', 'correct translation'), ('ny', 'not verified yet'), ('rt', 're-translated')], default='ny', max_length=2),
        ),
    ]
