# Generated by Django 5.0.4 on 2024-04-08 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=255)),
                ('solicitationnumber', models.IntegerField()),
                ('taskauthnumber', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('fax', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
