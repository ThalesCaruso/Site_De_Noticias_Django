# Generated by Django 4.1.7 on 2023-05-27 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_post_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postsituacao',
            name='post_situacao',
        ),
        migrations.AddField(
            model_name='post',
            name='tempo_leitura',
            field=models.CharField(default=30, max_length=2),
        ),
    ]
