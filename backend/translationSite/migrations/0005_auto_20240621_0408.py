# Generated by Django 3.2.25 on 2024-06-21 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translationSite', '0004_rename_output_ai_output_ai1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processed_output_ai',
            name='rfk',
        ),
        migrations.RemoveField(
            model_name='project1',
            name='author',
        ),
        migrations.DeleteModel(
            name='output_AI1',
        ),
        migrations.DeleteModel(
            name='processed_output_AI',
        ),
        migrations.DeleteModel(
            name='project1',
        ),
    ]
