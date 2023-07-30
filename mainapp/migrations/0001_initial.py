# Generated by Django 4.2.3 on 2023-07-24 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('nombrePersonaje', models.CharField(max_length=50)),
                ('apellidoPersonaje', models.CharField(max_length=50)),
                ('vivo', models.BooleanField()),
                ('fechaMuerte', models.CharField(max_length=50)),
            ],
        ),
    ]
