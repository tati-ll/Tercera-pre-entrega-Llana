# Generated by Django 4.2.3 on 2023-07-26 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Alumno",
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
                ("apellido", models.CharField(max_length=256)),
                ("nombre", models.CharField(max_length=256)),
                ("email", models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Material",
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
                ("nombre", models.CharField(max_length=256)),
                ("marca", models.CharField(max_length=256)),
                ("color", models.CharField(max_length=256)),
                ("composicion", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Taller",
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
                ("nombre", models.CharField(max_length=256)),
                ("profesor", models.CharField(max_length=256)),
                ("fecha", models.DateField()),
                ("descripcion", models.TextField(blank=True)),
                ("cupos", models.IntegerField(default=5)),
            ],
        ),
    ]
