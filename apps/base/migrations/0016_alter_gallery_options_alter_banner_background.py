# Generated by Django 5.0.3 on 2024-03-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_banner_image_1'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Галерея', 'verbose_name_plural': 'Галереи'},
        ),
        migrations.AlterField(
            model_name='banner',
            name='background',
            field=models.ImageField(upload_to='media6', verbose_name='Фото'),
        ),
    ]