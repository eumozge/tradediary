# Generated by Django 4.2.2 on 2023-06-13 06:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import helpers.db.fields
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=12, default=0, max_digits=20, verbose_name='pnl')),
                ('creation_date', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='creation date')),
            ],
            options={
                'verbose_name': 'trade',
                'verbose_name_plural': 'trades',
            },
        ),
        migrations.CreateModel(
            name='PositionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', helpers.db.fields.LowerCharField(unique=True)),
            ],
            options={
                'verbose_name': 'position type',
                'verbose_name_plural': 'position types',
            },
        ),
        migrations.CreateModel(
            name='PositionTypeResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', helpers.db.fields.LowerCharField(unique=True)),
            ],
            options={
                'verbose_name': 'type result',
                'verbose_name_plural': 'type results',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', helpers.db.fields.LowerCharField(unique=True)),
            ],
            options={
                'verbose_name': 'status',
                'verbose_name_plural': 'statuses',
            },
        ),
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', helpers.db.fields.LowerCharField(unique=True)),
            ],
            options={
                'verbose_name': 'symbol',
                'verbose_name_plural': 'symbols',
            },
        ),
        migrations.CreateModel(
            name='PositionResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=12, default=0, max_digits=20, verbose_name='price')),
                ('percent', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='percent')),
                ('pnl', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='pnl')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trades.position', verbose_name='trade')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trades.positiontyperesult', verbose_name='type')),
            ],
            options={
                'verbose_name': 'result',
                'verbose_name_plural': 'results',
            },
        ),
        migrations.CreateModel(
            name='PositionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='trades/images/', verbose_name='image')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trades.position', verbose_name='position')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
        ),
        migrations.AddField(
            model_name='position',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trades.status', verbose_name='status'),
        ),
        migrations.AddField(
            model_name='position',
            name='symbol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trades.symbol', verbose_name='symbol'),
        ),
        migrations.AddField(
            model_name='position',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trades.positiontype', verbose_name='type'),
        ),
    ]