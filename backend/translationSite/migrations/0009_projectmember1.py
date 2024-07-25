# Generated by Django 3.2.25 on 2024-07-25 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('translationSite', '0008_auto_20240725_0715'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectMember1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_type', models.CharField(choices=[('read', 'Read'), ('write', 'Write'), ('delete', 'Delete')], max_length=50)),
                ('granted_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='translationSite.project')),
            ],
        ),
    ]
