# Generated by Django 4.2.5 on 2023-10-11 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0061_jobapplication_companyname_jobapplication_job_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='adminstu',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='company',
        ),
    ]
