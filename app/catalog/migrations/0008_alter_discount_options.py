# Generated by Django 3.2.10 on 2023-07-29 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_alter_discount_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="discount",
            options={"verbose_name": "Акция", "verbose_name_plural": "Акции"},
        ),
    ]
