# Generated by Django 2.2.5 on 2019-10-11 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0008_remove_jobgrade_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]