# Generated by Django 3.2.7 on 2021-09-20 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0003_auto_20210920_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puja',
            name='valorpuja',
            field=models.TextField(),
        ),
    ]