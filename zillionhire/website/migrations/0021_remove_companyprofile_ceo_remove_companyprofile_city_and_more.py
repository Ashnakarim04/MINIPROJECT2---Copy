# Generated by Django 4.2.5 on 2023-10-01 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_remove_jobs_criteria_jobs_job_descriptions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyprofile',
            name='ceo',
        ),
        migrations.RemoveField(
            model_name='companyprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='companyprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='companyprofile',
            name='district',
        ),
        migrations.RemoveField(
            model_name='companyprofile',
            name='headquarter',
        ),
        migrations.RemoveField(
            model_name='companyprofile',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='companyprofile',
            name='state',
        ),
    ]
