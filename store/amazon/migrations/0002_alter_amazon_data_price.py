# Generated by Django 4.0.3 on 2022-03-21 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazon_data',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
