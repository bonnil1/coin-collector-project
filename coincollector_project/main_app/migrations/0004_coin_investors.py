# Generated by Django 5.0.4 on 2024-05-13 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_investor_alter_purchase_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='investors',
            field=models.ManyToManyField(to='main_app.investor'),
        ),
    ]