# Generated by Django 5.0.2 on 2024-03-11 08:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_commande_total'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commande',
            options={'ordering': ['-date_commande']},
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category'),
        ),
    ]