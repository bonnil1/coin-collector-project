# Generated by Django 5.0.4 on 2024-05-01 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('description', models.TextField(max_length=250)),
            ],
        ),
    ]
