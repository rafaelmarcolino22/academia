# Generated by Django 3.1.3 on 2021-01-24 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alunotreino',
            name='repeticao',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
