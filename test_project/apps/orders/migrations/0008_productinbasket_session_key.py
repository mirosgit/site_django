# Generated by Django 2.2.6 on 2019-11-16 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_productinbasket'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbasket',
            name='session_key',
            field=models.CharField(default=-1.0, max_length=128),
            preserve_default=False,
        ),
    ]
