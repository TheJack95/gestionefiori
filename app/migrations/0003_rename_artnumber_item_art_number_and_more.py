# Generated by Django 4.1.5 on 2023-01-29 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_item_originalprice_item_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='artNumber',
            new_name='art_number',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='eanCode',
            new_name='ean_code',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='imageName',
            new_name='image_name',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='imageUrl',
            new_name='image_url',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='originalPrice',
            new_name='original_price',
        ),
    ]