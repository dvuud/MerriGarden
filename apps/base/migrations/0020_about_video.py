# Generated by Django 5.0.3 on 2024-03-28 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_news_item_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='video',
            field=models.URLField(default=1, verbose_name='Видео(YouTube)'),
            preserve_default=False,
        ),
    ]
