# Generated by Django 4.2 on 2023-04-23 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libri', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='titolo',
            field=models.CharField(max_length=30),
        ),
    ]
