# Generated by Django 3.1.1 on 2020-09-27 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('nid_or_birth_certificate', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=3)),
                ('address', models.TextField()),
                ('contact_number', models.CharField(max_length=15)),
            ],
        ),
    ]
