# Generated by Django 3.2 on 2022-03-06 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latte', '0005_alter_quest_author'),
        ('accounts', '0008_auto_20220302_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='my_quests',
            field=models.ManyToManyField(related_name='my_quests', to='latte.Quest'),
        ),
    ]
