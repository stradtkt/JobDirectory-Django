# Generated by Django 2.1.2 on 2018-10-27 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0017_user_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(default='US', max_length=255),
        ),
    ]