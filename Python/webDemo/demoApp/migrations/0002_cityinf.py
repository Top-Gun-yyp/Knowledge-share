# Generated by Django 2.1.1 on 2018-10-27 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityInf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CityName', models.CharField(max_length=100)),
                ('CityAdd', models.CharField(max_length=100)),
            ],
        ),
    ]
