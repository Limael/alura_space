# Generated by Django 5.1 on 2024-08-15 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('GALAXIA', 'Galáxia'), ('PLANETA', 'Planeta'), ('ESTRELA', 'Estrela')], default='', max_length=100),
        ),
    ]
