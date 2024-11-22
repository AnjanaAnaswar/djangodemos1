# Generated by Django 5.1.2 on 2024-10-20 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('year', models.IntegerField()),
                ('image', models.ImageField(upload_to='images')),
                ('details', models.TextField(max_length=100, null=True)),
            ],
        ),
    ]
