# Generated by Django 3.0.5 on 2020-04-11 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0002_auto_20200411_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='publish_time',
            field=models.DateField(blank=True, max_length=200, null=True),
        ),
    ]
