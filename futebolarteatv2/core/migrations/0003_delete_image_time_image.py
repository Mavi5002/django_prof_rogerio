# Generated by Django 5.0.2 on 2024-02-28 18:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_image"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Image",
        ),
        migrations.AddField(
            model_name="time",
            name="image",
            field=models.ImageField(null=True, upload_to="imagem"),
        ),
    ]
