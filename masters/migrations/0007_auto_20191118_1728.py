# Generated by Django 2.2.4 on 2019-11-18 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0006_auto_20191114_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='locationname',
            new_name='location',
        ),
    ]
