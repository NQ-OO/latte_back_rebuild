# Generated by Django 3.2 on 2022-02-05 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='year',
            new_name='admission_year',
        ),
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.TextField(null=True),
        ),
    ]