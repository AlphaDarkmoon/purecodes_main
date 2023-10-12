# Generated by Django 4.2.6 on 2023-10-12 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purecodes_app', '0002_alter_post_options_alter_post_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='code_url',
            field=models.URLField(default='404.com'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_by',
            field=models.CharField(help_text="creator's name", max_length=225),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_url',
            field=models.URLField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Image_not_available.png/640px-Image_not_available.png'),
        ),
    ]
