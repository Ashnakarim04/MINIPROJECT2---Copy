# Generated by Django 4.2.5 on 2023-10-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0046_alter_jobs_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='cname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='jname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]