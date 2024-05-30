# Generated by Django 5.0.2 on 2024-05-30 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.CharField(max_length=10)),
                ('ficha', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'alumno',
                'verbose_name_plural': 'alumnos',
            },
        ),
    ]