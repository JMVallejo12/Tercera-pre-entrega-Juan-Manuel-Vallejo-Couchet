# Generated by Django 4.2.3 on 2023-07-27 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_temporada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suscriptor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreSuscriptor', models.CharField(max_length=50)),
            ],
        ),
    ]