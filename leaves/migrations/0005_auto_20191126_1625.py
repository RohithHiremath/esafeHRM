# Generated by Django 2.2.5 on 2019-11-26 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pim', '0014_auto_20191126_1313'),
        ('leaves', '0004_auto_20191121_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_list',
            name='document',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
    ]