# Generated by Django 3.2 on 2021-04-28 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20210427_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_quantity',
        ),
    ]
