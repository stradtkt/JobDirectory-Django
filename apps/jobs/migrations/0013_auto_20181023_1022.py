# Generated by Django 2.1.2 on 2018-10-23 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_blog_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=0, upload_to=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='image1',
            field=models.ImageField(default=0, upload_to=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='image2',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]
