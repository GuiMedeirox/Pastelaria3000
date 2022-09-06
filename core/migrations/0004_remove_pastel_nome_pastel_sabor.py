# Generated by Django 4.1 on 2022-09-06 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_pastel_pastelpedido_remove_pizzapedida_idpedido_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pastel',
            name='nome',
        ),
        migrations.AddField(
            model_name='pastel',
            name='sabor',
            field=models.CharField(default=None, max_length=255, verbose_name='Sabor'),
        ),
    ]
