# Generated by Django 3.1.3 on 2020-11-18 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('long_rent', models.FloatField()),
                ('short_rent', models.FloatField()),
                ('category', models.CharField(max_length=50)),
                ('accessries', models.CharField(max_length=100)),
            ],
        ),
    ]