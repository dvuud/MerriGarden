# Generated by Django 5.0.3 on 2024-03-24 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_rename_full_name_post_fullname_alter_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('background', models.ImageField(upload_to='media6', verbose_name='Фон')),
                ('image', models.ImageField(upload_to='media7', verbose_name='Фото')),
                ('image_1', models.ImageField(upload_to='media7', verbose_name='Первое фото')),
                ('image_2', models.ImageField(upload_to='media8', verbose_name='Второе фото')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name_plural': 'Баннеры',
            },
        ),
    ]
