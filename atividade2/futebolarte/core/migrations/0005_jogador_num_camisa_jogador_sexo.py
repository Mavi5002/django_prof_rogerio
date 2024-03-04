# Generated by Django 5.0.2 on 2024-03-02 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_jogador'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogador',
            name='num_camisa',
            field=models.PositiveIntegerField(default=False),
        ),
        migrations.AddField(
            model_name='jogador',
            name='sexo',
            field=models.CharField(choices=[('F', 'FERMININO'), ('M', 'MASCULINO')], max_length=100, null=True),
        ),
    ]
