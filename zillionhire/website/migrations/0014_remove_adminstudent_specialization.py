# Generated by Django 4.2.5 on 2023-09-25 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_adminstudent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminstudent',
            name='specialization',
        ),
    ]
