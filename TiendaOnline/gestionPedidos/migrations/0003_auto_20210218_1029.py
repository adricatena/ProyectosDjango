# Generated by Django 3.1.6 on 2021-02-18 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0002_auto_20210218_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='La direccion'),
        ),
    ]