# Generated by Django 4.1.3 on 2023-01-04 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecurrringOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('title', models.CharField(max_length=90)),
                ('pricing', models.CharField(max_length=70)),
            ],
        ),
    ]
