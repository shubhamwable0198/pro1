# Generated by Django 5.0.7 on 2024-07-12 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('salary', models.IntegerField()),
                ('dob', models.DateField()),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
