# Generated by Django 5.1 on 2024-09-13 17:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_rename_autor_livro_autores"),
    ]

    operations = [
        migrations.CreateModel(
            name="Compra",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "status",
                    models.IntegerField(
                        choices=[(1, "Carrinho"), (2, "Realizado"), (3, "Pago"), (4, "Entregue")], default=1
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="compras", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ItensCompra",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("quantidade", models.IntegerField(default=1)),
                (
                    "compra",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="itens", to="core.compra"
                    ),
                ),
                (
                    "livro",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="+", to="core.livro"),
                ),
            ],
        ),
    ]
