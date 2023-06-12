# Generated by Django 4.2.2 on 2023-06-29 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0005_rename_price_position_opening_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positionimage',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trades.position', verbose_name='position'),
        ),
        migrations.AlterField(
            model_name='positionresult',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trades.position', verbose_name='trade'),
        ),
    ]
