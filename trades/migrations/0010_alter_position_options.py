# Generated by Django 4.2.2 on 2023-06-30 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0009_alter_position_options_alter_positiontype_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ('-creation_date',), 'verbose_name': 'trade', 'verbose_name_plural': 'trades'},
        ),
    ]
