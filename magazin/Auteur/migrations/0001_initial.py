# Generated by Django 4.0.4 on 2022-05-29 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auteur',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=30)),
                ('Tel', models.IntegerField()),
                ('Cin', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
            ],
        ),
    ]
