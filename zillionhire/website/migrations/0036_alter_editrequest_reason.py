# Generated by Django 4.2.5 on 2023-10-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0035_editrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editrequest',
            name='reason',
            field=models.CharField(default=' ', max_length=20),
        ),
    ]