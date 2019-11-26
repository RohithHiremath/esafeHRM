# Generated by Django 2.2.4 on 2019-11-22 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pim', '0008_auto_20191121_1249'),
        ('leaves', '0003_auto_20191120_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fromdate', models.DateField()),
                ('Todate', models.DateField()),
                ('NumberOfLeaves', models.SmallIntegerField(default=1)),
                ('AppliedDate', models.DateTimeField()),
                ('Status', models.SmallIntegerField(default=1)),
                ('Reason', models.CharField(blank=True, max_length=100)),
                ('FullorHalfday', models.SmallIntegerField(default=1)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pim.Personal_details')),
                ('leave_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaves.Leavetype')),
            ],
        ),
    ]
