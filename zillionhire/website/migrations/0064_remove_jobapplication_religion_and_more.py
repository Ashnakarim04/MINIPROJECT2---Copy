# Generated by Django 4.2.5 on 2023-10-11 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0063_alter_jobapplication_job_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='religion',
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='c_backlog',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
