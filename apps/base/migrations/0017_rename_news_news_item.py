# Generated by Django 5.0.3 on 2024-03-27 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_gallery_options_alter_banner_background'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='News_item',
        ),
    ]