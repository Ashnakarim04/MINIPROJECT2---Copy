# Generated by Django 4.2.4 on 2023-09-12 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='city',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='country',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='district',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='pincode',
            field=models.CharField(default='default', max_length=15),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='state',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='website',
            field=models.CharField(default='default', max_length=100),
        ),
    ]
