# Generated by Django 4.0.6 on 2024-03-24 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('icon', models.ImageField(upload_to='category_icons')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
    ]