# Generated by Django 3.2.10 on 2023-07-19 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_remove_discount_comments_comments_discounts"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Comments",
        ),
    ]
