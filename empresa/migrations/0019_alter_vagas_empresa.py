# Generated by Django 4.1.3 on 2022-11-15 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0018_remove_empresa_nicho_mercado_empresa_nicho_mercado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagas',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa'),
        ),
    ]
