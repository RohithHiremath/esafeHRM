# Generated by Django 2.2.5 on 2020-01-17 12:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0002_auto_20200117_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='payscale',
            name='experienceto',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='payscale',
            name='experincefrom',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='payscale',
            name='shortname',
            field=models.CharField(default='', max_length=3, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='payscale',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='payscale',
            name='payscalename',
            field=models.CharField(default='', max_length=50, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]