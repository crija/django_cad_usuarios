# Generated by Django 4.1.7 on 2023-06-13 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=240)),
                ('idade', models.IntegerField()),
            ],
        ),
    ]
