# Generated by Django 5.0.1 on 2024-03-10 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_rename_zipecode_commande_zipcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='total',
            field=models.CharField(default='500', max_length=200),
            preserve_default=False,
        ),
    ]
