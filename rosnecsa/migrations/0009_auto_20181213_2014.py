# Generated by Django 2.1.4 on 2018-12-13 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosnecsa', '0008_auto_20181213_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folio',
            name='fallas_detectadas_folio',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='folio',
            name='piezas_cambiadas_folio',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='folio',
            name='reparaciones_efectuadas_folio',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
