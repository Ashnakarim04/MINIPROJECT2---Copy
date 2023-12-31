# Generated by Django 4.2.5 on 2023-10-02 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_alter_studentprofile_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='academic_year',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='admission_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='cgpa',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='current_semester',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='nationality',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='permanent_address',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='present_address',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='religion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='tenth_cgpa',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='tenth_course',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='tenth_institution',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='twelfth_cgpa',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='twelfth_course',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='twelfth_institution',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='ug_cgpa',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='ug_course',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='ug_institution',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
