# Generated by Django 4.0 on 2021-12-20 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_services_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='state',
            new_name='city',
        ),
    ]