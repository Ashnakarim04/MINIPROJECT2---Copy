# Generated by Django 4.2.5 on 2023-09-27 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_studentprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='is_approved',
            field=models.BooleanField(default=True),
        ),
    ]
