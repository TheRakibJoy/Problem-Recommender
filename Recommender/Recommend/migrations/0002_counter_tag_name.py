# Generated by Django 4.2.6 on 2023-10-05 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recommend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='Tag_Name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
