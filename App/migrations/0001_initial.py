# Generated by Django 4.0.4 on 2022-04-12 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='namaz_time_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaz_name', models.CharField(max_length=50)),
                ('namaz_time', models.CharField(max_length=50)),
            ],
        ),
    ]