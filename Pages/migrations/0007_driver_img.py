# Generated by Django 3.1.7 on 2021-05-17 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0006_auto_20210514_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='img',
            field=models.CharField(default=1, max_length=200),
        ),
    ]
