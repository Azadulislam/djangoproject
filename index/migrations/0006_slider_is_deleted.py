# Generated by Django 4.0.5 on 2022-06-25 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_slider_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
