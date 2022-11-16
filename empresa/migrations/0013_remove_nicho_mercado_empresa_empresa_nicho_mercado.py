# Generated by Django 4.1.3 on 2022-11-14 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0012_remove_empresa_nicho_mercado_nicho_mercado_empresa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nicho_mercado',
            name='empresa',
        ),
        migrations.AddField(
            model_name='empresa',
            name='nicho_mercado',
            field=models.ManyToManyField(to='empresa.nicho_mercado'),
        ),
    ]
