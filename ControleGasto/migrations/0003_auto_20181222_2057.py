# Generated by Django 2.1.3 on 2018-12-22 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControleGasto', '0002_auto_20181222_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='vencimento',
            field=models.DateTimeField(),
        ),
    ]
