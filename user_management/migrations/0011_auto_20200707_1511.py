# Generated by Django 3.0.8 on 2020-07-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0010_auto_20200707_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='actived_at',
            field=models.DateTimeField(null=True),
        ),
    ]