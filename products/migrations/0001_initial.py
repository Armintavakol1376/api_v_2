# Generated by Django 4.2.2 on 2023-07-01 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('subtitle', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=13)),
            ],
        ),
    ]
