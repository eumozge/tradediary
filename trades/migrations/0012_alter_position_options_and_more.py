# Generated by Django 4.2.2 on 2023-06-30 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0011_alter_position_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ('-opening_date',), 'verbose_name': 'trade', 'verbose_name_plural': 'trades'},
        ),
        migrations.RenameField(
            model_name='position',
            old_name='opening_data',
            new_name='opening_date',
        ),
    ]
