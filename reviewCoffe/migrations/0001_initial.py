# Generated by Django 5.1.4 on 2025-01-11 14:41

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("companyCoffe", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="reviewCoffe",
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
                (
                    "stars",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, "Sua avaliação nao pode ser menor que 0 estrelas."
                            ),
                            django.core.validators.MaxValueValidator(
                                5, "Sua avaliação nao pode ser maior que 5 estrelas."
                            ),
                        ]
                    ),
                ),
                ("comment", models.TextField(blank=True, null=True)),
                (
                    "companycoffe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="review",
                        to="companyCoffe.companycoffe",
                    ),
                ),
            ],
        ),
    ]
