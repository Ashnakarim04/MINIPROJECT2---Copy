# Generated by Django 4.2.5 on 2023-10-02 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_alter_studentprofile_cgpa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='dob',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
