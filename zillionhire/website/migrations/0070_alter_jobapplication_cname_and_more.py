# Generated by Django 4.2.5 on 2023-10-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0069_alter_jobapplication_cname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='cname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='jname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]