# Generated by Django 2.1.4 on 2018-12-31 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControleGasto', '0004_auto_20181231_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='vencimento',
            field=models.DateTimeField(),
        ),
    ]
