# Generated by Django 2.1.2 on 2018-10-27 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0015_languages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='blog_category',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='user',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='BlogCategory',
        ),
    ]
