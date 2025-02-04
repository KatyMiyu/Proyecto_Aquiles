# Generated by Django 4.1.2 on 2024-07-13 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convenios_administrador',
            fields=[
                ('id_convenio_adm', models.AutoField(db_column='idConvenioAdm', primary_key=True, serialize=False)),
                ('nom_convenio_adm', models.CharField(max_length=50)),
                ('platos_convenio_adm', models.CharField(max_length=50)),
                ('modo_entrega', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estadisticas_administrador',
            fields=[
                ('id_estadisticas', models.AutoField(db_column='idEstadisticas', primary_key=True, serialize=False)),
                ('ventas_mes', models.CharField(max_length=50)),
                ('productos_vendidos', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Nav_administrador',
            fields=[
                ('id_navbar_adm', models.AutoField(db_column='idNavAdm', primary_key=True, serialize=False)),
                ('nav_adm', models.CharField(max_length=20)),
                ('url_adm', models.CharField(default='default_value', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Platos_administrador',
            fields=[
                ('id_platos_adm', models.AutoField(db_column='idPlatosAdm', primary_key=True, serialize=False)),
                ('nom_platos_adm', models.CharField(max_length=50)),
                ('precio_platos_adm', models.CharField(max_length=20)),
                ('oferta_platos_adm', models.CharField(max_length=20)),
                ('detalles_platos_adm', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores_administrador',
            fields=[
                ('id_proveedor_adm', models.AutoField(db_column='idProveedoresAdm', primary_key=True, serialize=False)),
                ('nom_proveedor_adm', models.CharField(max_length=50)),
                ('platos_adm', models.CharField(max_length=100)),
                ('ofertas_adm', models.CharField(max_length=50)),
            ],
        ),
    ]
