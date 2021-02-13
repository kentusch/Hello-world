# Generated by Django 3.1.5 on 2021-02-04 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=150)),
                ('permission', models.BooleanField()),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
    ]
