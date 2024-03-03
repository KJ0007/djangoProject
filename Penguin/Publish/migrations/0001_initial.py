# Generated by Django 5.0.2 on 2024-02-23 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PublisherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=10)),
                ('bname', models.CharField(max_length=10)),
                ('bpage', models.IntegerField()),
                ('bprice', models.FloatField()),
                ('aemail', models.EmailField(max_length=254)),
            ],
        ),
    ]
