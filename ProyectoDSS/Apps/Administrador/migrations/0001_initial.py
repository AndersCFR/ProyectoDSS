# Generated by Django 3.2.7 on 2021-09-19 18:45

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('idadministrador', models.AutoField(primary_key=True, serialize=False)),
                ('nombreadmin', models.CharField(max_length=1024)),
                ('passwordadmin', models.CharField(max_length=1024)),
            ],
            managers=[
                ('empAuth_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('idproyecto', models.AutoField(primary_key=True, serialize=False)),
                ('nombresubasta', models.CharField(max_length=1024)),
                ('descripcion', models.CharField(max_length=1024)),
                ('estadoproyecto', models.BooleanField()),
                ('idadministrador', models.ForeignKey(db_column='idadministrador', on_delete=django.db.models.deletion.DO_NOTHING, to='Administrador.administrador')),
            ],
        ),
        migrations.CreateModel(
            name='Requerimiento',
            fields=[
                ('idrequerimiento', models.AutoField(primary_key=True, serialize=False)),
                ('descripcionrequerimiento', models.TextField()),
                ('presupuestoreferencial', models.DecimalField(decimal_places=2, max_digits=6)),
                ('idproyecto', models.ForeignKey(db_column='idproyecto', on_delete=django.db.models.deletion.DO_NOTHING, to='Administrador.proyecto')),
            ],
        ),
    ]
