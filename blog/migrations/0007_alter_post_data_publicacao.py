# Generated by Django 4.1.7 on 2023-05-15 23:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 5, 15, 23, 8, 8, 101399, tzinfo=datetime.timezone.utc)),
        ),
    ]