# Generated by Django 4.2.5 on 2023-10-11 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0067_rename_companyname_jobapplication_cname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='c_cgpa',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='c_backlog',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
