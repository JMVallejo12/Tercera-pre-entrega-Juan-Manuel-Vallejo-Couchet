# Generated by Django 4.2.3 on 2023-07-24 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temporada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTemporada', models.CharField(max_length=50)),
                ('numeroCapitulos', models.IntegerField()),
                ('fechaEmision', models.CharField(max_length=50)),
            ],
        ),
    ]