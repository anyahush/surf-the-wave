# Generated by Django 3.2.13 on 2022-05-08 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_rename_original_bag_order_original_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]