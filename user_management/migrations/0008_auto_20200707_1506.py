# Generated by Django 3.0.8 on 2020-07-07 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0007_auto_20200707_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useractivity',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserActivity',
        ),
    ]