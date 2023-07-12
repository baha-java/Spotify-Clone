# Generated by Django 4.2.1 on 2023-05-10 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spotify', '0014_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.TextField(max_length=50)),
                ('birth_date', models.DateTimeField(auto_now=True)),
                ('gender', models.TextField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]