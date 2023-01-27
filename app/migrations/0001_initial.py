# Generated by Django 4.1.5 on 2023-01-27 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artNumber', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('eanCode', models.CharField(max_length=50)),
                ('imageName', models.CharField(max_length=200)),
                ('imageUrl', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'items',
            },
        ),
    ]
