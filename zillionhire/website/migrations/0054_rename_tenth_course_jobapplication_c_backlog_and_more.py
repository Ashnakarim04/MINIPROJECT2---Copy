# Generated by Django 4.2.5 on 2023-10-08 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0053_alter_studentprofile_dob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobapplication',
            old_name='tenth_course',
            new_name='c_backlog',
        ),
        migrations.RenameField(
            model_name='jobapplication',
            old_name='twelfth_course',
            new_name='c_cgpa',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='admission_no',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='cgpa',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='course',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='current_semester',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='department',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='reset_password',
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='area_code',
            field=models.CharField(blank=True, choices=[('+1 (United States)', '+1 (United States)'), ('+44 (United Kingdom)', '+44 (United Kingdom)'), ('+91 (India)', '+91 (India)'), ('+61 (Australia)', '+61 (Australia)')], max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='c_course',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='c_institution',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='c_university',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='companydetails',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='crime',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Yes', 'Yes')], max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='doc',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='dtoc',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='jobresp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='nature',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='newcert',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='newcourse',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='period',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='skills',
            field=models.CharField(blank=True, max_length=700, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='tenth_board',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='twelfth_board',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='ug_university',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='workexperience',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Yes', 'Yes')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='gender',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
