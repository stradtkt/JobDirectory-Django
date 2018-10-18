# Generated by Django 2.1.2 on 2018-10-18 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_remove_pastjobs_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastjobs',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile', to='jobs.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='past_jobs', to='jobs.User'),
        ),
    ]
