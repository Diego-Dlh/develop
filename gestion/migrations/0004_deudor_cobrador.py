# Generated by Django 5.2.4 on 2025-07-25 23:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_remove_prestamo_monto_total_alter_deudor_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deudor',
            name='cobrador',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='deudores', to='gestion.usuario'),
            preserve_default=False,
        ),
    ]
