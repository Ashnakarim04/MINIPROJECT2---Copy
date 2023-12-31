# Generated by Django 4.2.5 on 2023-10-08 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0051_alter_studentprofile_ug_cgpa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='dob',
            field=models.DateField(blank=True, max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_no', models.CharField(blank=True, max_length=20, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('dob', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=50, null=True)),
                ('nationality', models.CharField(blank=True, max_length=50, null=True)),
                ('religion', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('reset_password', models.CharField(blank=True, max_length=128, null=True)),
                ('email', models.EmailField(default=' ', max_length=254)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('present_address', models.TextField(blank=True, null=True)),
                ('permanent_address', models.TextField(blank=True, null=True)),
                ('course', models.CharField(blank=True, choices=[('B.Tech', 'B.Tech'), ('MCA', 'MCA')], max_length=50, null=True)),
                ('department', models.CharField(blank=True, choices=[('ECE', 'ECE'), ('CSE', 'CSE'), ('Integrated MCA', 'Integrated MCA'), ('Regular MCA', 'Regular MCA')], max_length=100, null=True)),
                ('academic_year', models.CharField(blank=True, max_length=10, null=True)),
                ('current_semester', models.CharField(blank=True, max_length=10, null=True)),
                ('cgpa', models.FloatField(blank=True, null=True)),
                ('twelfth_institution', models.CharField(blank=True, max_length=100, null=True)),
                ('twelfth_cgpa', models.FloatField(blank=True, null=True)),
                ('twelfth_course', models.CharField(blank=True, max_length=100, null=True)),
                ('twelfth_certificate_upload', models.FileField(blank=True, null=True, upload_to='images/')),
                ('tenth_institution', models.CharField(blank=True, max_length=100, null=True)),
                ('tenth_cgpa', models.FloatField(blank=True, null=True)),
                ('tenth_course', models.CharField(blank=True, max_length=100, null=True)),
                ('tenth_certificate_upload', models.FileField(blank=True, null=True, upload_to='images/')),
                ('ug_institution', models.CharField(blank=True, max_length=100, null=True)),
                ('ug_cgpa', models.CharField(blank=True, max_length=100, null=True)),
                ('ug_course', models.CharField(blank=True, max_length=100, null=True)),
                ('ug_certificate_upload', models.FileField(blank=True, null=True, upload_to='images/')),
                ('adminstu', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.adminstudent')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
