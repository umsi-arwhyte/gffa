# Generated by Django 3.1.8 on 2021-05-08 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_auto_20210506_2222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filmcharacter',
            options={'managed': False, 'ordering': ['film', 'character'], 'verbose_name': 'Film Character', 'verbose_name_plural': 'Film Characters'},
        ),
        migrations.AlterModelOptions(
            name='filmplanet',
            options={'managed': False, 'ordering': ['film', 'planet'], 'verbose_name': 'Film Planet', 'verbose_name_plural': 'Film Planets'},
        ),
        migrations.AlterModelOptions(
            name='filmstarship',
            options={'managed': False, 'ordering': ['film', 'starship'], 'verbose_name': 'Film Starship', 'verbose_name_plural': 'Film Starships'},
        ),
        migrations.AlterModelOptions(
            name='starship',
            options={'managed': False, 'ordering': ['name'], 'verbose_name': 'Starship', 'verbose_name_plural': 'Starships'},
        ),
    ]
