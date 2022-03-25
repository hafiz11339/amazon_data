# Generated by Django 4.0.3 on 2022-03-21 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='amazon_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=10, max_digits=10)),
                ('link', models.CharField(max_length=150)),
            ],
        ),
    ]
