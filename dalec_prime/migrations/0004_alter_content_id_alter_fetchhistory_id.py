# Generated by Django 4.2 on 2023-06-21 08:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dalec_prime", "0003_auto_20211109_1615"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="fetchhistory",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
