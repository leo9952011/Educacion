# Generated by Django 4.0.2 on 2022-05-17 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=60)),
                ('promocionable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCiudad', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('angno', models.CharField(max_length=10)),
                ('detalle', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePais', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.IntegerField()),
                ('nombrePersona', models.CharField(max_length=60)),
                ('apellidoPersona', models.CharField(max_length=60)),
                ('fechaNac', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=12)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.persona')),
            ],
        ),
        migrations.CreateModel(
            name='TipoCalificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCarrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Situacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=60)),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.asignatura')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.profesor')),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProvincia', models.CharField(max_length=60)),
                ('Pais', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.pais')),
            ],
        ),
        migrations.AddField(
            model_name='ciudad',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.provincia'),
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=60)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.tipocarrera')),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.CharField(max_length=30)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.persona')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.tipocargo')),
            ],
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField()),
                ('observacion', models.CharField(max_length=200)),
                ('Alumno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.alumno')),
                ('Asignatura', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.asignatura')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.tipocalificacion')),
            ],
        ),
        migrations.CreateModel(
            name='Auxiliar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.persona')),
            ],
        ),
        migrations.AddField(
            model_name='asignatura',
            name='carrera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.carrera'),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.curso'),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='matricula',
            field=models.ManyToManyField(to='direccion.Alumno'),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.profesor'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.persona'),
        ),
    ]
