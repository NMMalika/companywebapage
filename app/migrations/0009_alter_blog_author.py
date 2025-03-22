# Generated by Django 5.0.6 on 2025-03-20 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0008_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.author"
            ),
        ),
    ]
