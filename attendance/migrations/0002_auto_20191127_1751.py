# Generated by Django 2.2.4 on 2019-11-27 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tardinessdetails',
            name='OTPayment',
            field=models.SmallIntegerField(default=3),
        ),
        migrations.AddField(
            model_name='tardinessdetails',
            name='OTcompensatorytype',
            field=models.SmallIntegerField(default=2),
        ),
        migrations.AddField(
            model_name='tardinessdetails',
            name='minimumHoursForOT',
            field=models.SmallIntegerField(default=2),
        ),
    ]