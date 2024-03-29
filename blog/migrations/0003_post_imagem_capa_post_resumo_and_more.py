# Generated by Django 4.1.7 on 2023-05-02 23:38

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_conteudo_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagem_capa',
            field=models.ImageField(blank=True, null=True, upload_to='static/blog/'),
        ),
        migrations.AddField(
            model_name='post',
            name='resumo',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 5, 2, 23, 38, 8, 577538, tzinfo=datetime.timezone.utc)),
        ),
    ]
