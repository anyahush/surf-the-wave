# Generated by Django 3.2.13 on 2022-05-22 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_productreview_review_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productreview',
            name='review_title',
        ),
    ]