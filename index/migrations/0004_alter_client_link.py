# Generated by Django 4.0.5 on 2022-06-22 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='link',
            field=models.CharField(max_length=200),
        ),
    ]
