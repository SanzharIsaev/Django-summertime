# Generated by Django 4.2.14 on 2024-07-26 15:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Catalog",
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
                    "name",
                    models.CharField(max_length=50, verbose_name="Название каталога"),
                ),
                ("text", models.TextField(verbose_name="Markdown редактор")),
            ],
            options={
                "verbose_name": "Каталог",
                "verbose_name_plural": "Каталоги",
            },
        ),
    ]
