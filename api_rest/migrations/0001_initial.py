# Generated by Django 5.1.2 on 2024-10-20 20:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=255)),
                ('telefone', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=255)),
                ('descricao', models.TextField(blank=True, default='')),
                ('quantidade', models.IntegerField(default=0)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('criado_em', models.DateField(auto_now_add=True)),
                ('editado_em', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=255)),
                ('descricao', models.TextField(blank=True, default='')),
                ('quantidade', models.IntegerField(default=0)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('criado_em', models.DateField(auto_now_add=True)),
                ('editado_em', models.DateField(auto_now=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.produtos')),
            ],
        ),
    ]
