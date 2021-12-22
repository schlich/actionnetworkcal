# Generated by Django 4.0 on 2021-12-22 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start', models.DateTimeField()),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('zip', models.IntegerField(blank=True, null=True)),
                ('group', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.URLField()),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
    ]