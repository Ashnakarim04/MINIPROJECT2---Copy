# Generated by Django 4.2.5 on 2023-10-02 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_alter_companyprofile_companyname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
