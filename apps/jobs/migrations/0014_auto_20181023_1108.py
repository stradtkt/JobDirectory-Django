# Generated by Django 2.1.2 on 2018-10-23 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_auto_20181023_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='comment',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
