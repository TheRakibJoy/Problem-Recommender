# Generated by Django 4.2.3 on 2023-10-05 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Dataset', '0002_delete_handle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Handle',
            fields=[
                ('handle', models.CharField(max_length=40, primary_key=True, serialize=False)),
            ],
        ),
    ]
