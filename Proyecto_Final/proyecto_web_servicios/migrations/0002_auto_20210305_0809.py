# Generated by Django 3.1.5 on 2021-03-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_web_servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro_cliente',
            name='telefono',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='registro_servicios',
            name='telefono',
            field=models.CharField(max_length=10),
        ),
    ]
