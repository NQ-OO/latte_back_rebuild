# Generated by Django 3.2 on 2022-02-02 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='year',
            new_name='admission_year',
        ),
    ]
