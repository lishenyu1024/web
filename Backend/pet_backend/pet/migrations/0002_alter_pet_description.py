# Generated by Django 4.0.6 on 2024-03-15 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]