# Generated by Django 4.2.7 on 2024-03-13 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empid', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('DOJ', models.CharField(default=0, max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
