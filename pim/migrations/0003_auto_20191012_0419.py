# Generated by Django 2.2.5 on 2019-10-12 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pim', '0002_auto_20191011_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_details',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='personal_details',
            name='date_of_permanency',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='personal_details',
            name='joined_date',
            field=models.DateField(),
        ),
    ]
