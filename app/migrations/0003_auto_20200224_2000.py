# Generated by Django 3.0.3 on 2020-02-24 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200224_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='tags',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
