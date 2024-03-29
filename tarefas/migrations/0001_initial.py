# Generated by Django 4.2.9 on 2024-01-25 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tarefa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descricao", models.CharField(max_length=200)),
                ("criacao", models.DateTimeField(auto_now_add=True)),
                (
                    "categoria",
                    models.CharField(
                        choices=[
                            ("urgente", "Urgente"),
                            ("importante", "Importante"),
                            ("precisa ser feito", "Precisa ser feito"),
                        ],
                        default="importante",
                        max_length=25,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("concluído", "Concluído"),
                            ("pendente", "Pendente"),
                            ("adiado", "Adiado"),
                        ],
                        default="pendente",
                        max_length=25,
                    ),
                ),
            ],
        ),
    ]
