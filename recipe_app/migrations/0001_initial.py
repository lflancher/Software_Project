# Generated by Django 4.2.5 on 2023-11-03 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('short_desc', models.CharField(max_length=414)),
                ('instruction', models.CharField(max_length=3000)),
                ('ingredients', models.CharField(max_length=2000)),
                
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=35)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
