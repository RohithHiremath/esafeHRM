# Generated by Django 2.2.5 on 2019-11-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0003_upload_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_list',
            name='document',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
