# Generated by Django 4.2.5 on 2023-10-07 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0047_alter_jobs_cname_alter_jobs_jname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]