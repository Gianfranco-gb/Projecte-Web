# Generated by Django 3.1.7 on 2021-05-14 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0005_auto_20210514_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='num_scuderias',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='season',
            name='year',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='season',
            name='scuderia_champion',
            field=models.CharField(max_length=200),
        ),
    ]
