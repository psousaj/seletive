# Generated by Django 4.1.3 on 2022-11-14 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0016_alter_nicho_mercado_nicho'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='nicho_mercado',
        ),
        migrations.AddField(
            model_name='empresa',
            name='nicho_mercado',
            field=models.ManyToManyField(to='empresa.nicho_mercado'),
        ),
    ]
