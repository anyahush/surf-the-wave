# Generated by Django 3.2.13 on 2022-05-21 13:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20220520_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='blog_comment',
            field=models.TextField(validators=[django.core.validators.MaxLengthValidator(250)]),
        ),
    ]
