# Generated by Django 4.0.5 on 2022-06-04 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_repay_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repay',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]