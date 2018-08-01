# Generated by Django 2.0.7 on 2018-07-30 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('muduryardimci', '0002_auto_20180730_1939'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notes',
            new_name='Note',
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='note',
            name='site_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='site_id', to='muduryardimci.Site'),
        ),
    ]