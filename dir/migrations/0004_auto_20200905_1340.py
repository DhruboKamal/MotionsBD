# Generated by Django 3.1 on 2020-09-05 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir', '0003_auto_20200905_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='date',
            field=models.DateField(),
        ),
    ]
