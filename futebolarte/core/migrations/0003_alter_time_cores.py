# Generated by Django 5.0.2 on 2024-02-27 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_time_ano_fundaçao_time_estado_time_tem_mundial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='cores',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]