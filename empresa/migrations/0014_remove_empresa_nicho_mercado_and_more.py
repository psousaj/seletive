# Generated by Django 4.1.3 on 2022-11-14 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0013_remove_nicho_mercado_empresa_empresa_nicho_mercado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='nicho_mercado',
        ),
        migrations.AlterField(
            model_name='nicho_mercado',
            name='nicho',
            field=models.CharField(max_length=300),
        ),
        migrations.AddField(
            model_name='empresa',
            name='nicho_mercado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='empresa.nicho_mercado'),
            preserve_default=False,
        ),
    ]