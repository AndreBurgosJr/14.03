# Generated by Django 5.0.3 on 2024-03-15 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='telefone',
            new_name='celular',
        ),
    ]
