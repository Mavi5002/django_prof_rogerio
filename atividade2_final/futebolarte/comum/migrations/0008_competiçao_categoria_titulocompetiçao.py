# Generated by Django 5.0.2 on 2024-03-02 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comum', '0007_rename_competiçoes_tp_competiçao_tipo_da_competição'),
    ]

    operations = [
        migrations.AddField(
            model_name='competiçao',
            name='categoria',
            field=models.CharField(choices=[('CP', 'Copa'), ('CPN', 'Campeonato')], max_length=32, null=True),
        ),
        migrations.CreateModel(
            name='TituloCompetiçao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.PositiveIntegerField(default=False)),
                ('resultado', models.CharField(choices=[('CP', 'Campeão'), ('VC', 'Vice-Campeão')], max_length=30, null=True)),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titulodoclube', to='comum.time')),
            ],
        ),
    ]
