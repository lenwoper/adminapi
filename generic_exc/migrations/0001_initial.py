# Generated by Django 4.1.3 on 2022-12-27 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=130)),
                ('roll', models.IntegerField()),
                ('city', models.CharField(max_length=290)),
            ],
        ),
    ]
