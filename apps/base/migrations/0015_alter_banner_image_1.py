# Generated by Django 5.0.3 on 2024-03-25 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_remove_banner_image_2_banner_title_for_video_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image_1',
            field=models.ImageField(upload_to='media7', verbose_name='фото'),
        ),
    ]