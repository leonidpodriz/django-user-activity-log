# Generated by Django 3.0 on 2021-04-05 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activity_log', '0007_auto_20210405_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitylog',
            name='username',
        ),
        migrations.AddField(
            model_name='activitylog',
            name='session_key',
            field=models.CharField(max_length=32, null=True, verbose_name='session'),
        ),
        migrations.AlterField(
            model_name='activitylog',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
