# Generated by Django 4.0.4 on 2022-05-25 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppViajeros', '0002_rename_subitulo_america_subtitulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Africa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('subtitulo', models.CharField(max_length=30)),
                ('cuerpo', models.CharField(max_length=500)),
                ('autor', models.CharField(max_length=50)),
                ('fecha', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Asia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('subtitulo', models.CharField(max_length=30)),
                ('cuerpo', models.CharField(max_length=500)),
                ('autor', models.CharField(max_length=50)),
                ('fecha', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Europa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('subtitulo', models.CharField(max_length=30)),
                ('cuerpo', models.CharField(max_length=500)),
                ('autor', models.CharField(max_length=50)),
                ('fecha', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Oceania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('subtitulo', models.CharField(max_length=30)),
                ('cuerpo', models.CharField(max_length=500)),
                ('autor', models.CharField(max_length=50)),
                ('fecha', models.CharField(max_length=30)),
            ],
        ),
    ]
