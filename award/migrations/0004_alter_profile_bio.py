# Generated by Django 3.2.7 on 2021-09-23 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(),
        ),
    ]
