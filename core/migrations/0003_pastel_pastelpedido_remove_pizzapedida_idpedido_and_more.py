# Generated by Django 4.1 on 2022-09-06 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_pizzapedida_has_ingrediente_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pastel',
            fields=[
                ('idPastel', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('precoBase', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PastelPedido',
            fields=[
                ('idPastelPedido', models.IntegerField(primary_key=True, serialize=False)),
                ('quantidade', models.IntegerField()),
                ('idPastel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pastel')),
            ],
        ),
        migrations.RemoveField(
            model_name='pizzapedida',
            name='idPedido',
        ),
        migrations.RemoveField(
            model_name='pizzapedida',
            name='idPizza',
        ),
        migrations.RemoveField(
            model_name='pizzapedida',
            name='idTamanho',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='idFornada',
        ),
        migrations.DeleteModel(
            name='Fornada',
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.DeleteModel(
            name='PizzaPedida',
        ),
        migrations.DeleteModel(
            name='Tamanho',
        ),
        migrations.AddField(
            model_name='pastelpedido',
            name='idPedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pedido'),
        ),
    ]
