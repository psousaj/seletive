# Generated by Django 4.1.3 on 2022-11-14 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0015_alter_nicho_mercado_nicho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nicho_mercado',
            name='nicho',
            field=models.CharField(max_length=300),
        ),
    ]
