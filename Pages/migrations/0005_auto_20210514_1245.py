# Generated by Django 3.1.7 on 2021-05-14 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0004_auto_20210513_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circuit',
            name='circuit_length',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='circuit',
            name='first_gp',
            field=models.CharField(max_length=20),
        ),
    ]