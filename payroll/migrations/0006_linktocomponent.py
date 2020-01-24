# Generated by Django 2.2.5 on 2020-01-18 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0005_assigninglevelstopayscale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linktocomponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.Salarycomponent')),
                ('payscale_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.PayScale')),
            ],
        ),
    ]
