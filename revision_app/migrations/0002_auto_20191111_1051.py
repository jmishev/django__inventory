# Generated by Django 2.2.6 on 2019-11-11 08:51

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revision_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
