# Generated by Django 3.0.5 on 2020-04-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=100)),
                ('fposition', models.CharField(max_length=30)),
                ('femail', models.EmailField(max_length=254)),
                ('fcontact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'funcionario',
            },
        ),
    ]
