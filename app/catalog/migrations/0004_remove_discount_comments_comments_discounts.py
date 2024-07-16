# Generated by Django 4.2.2 on 2023-07-06 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0003_comments_discount_comments"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="discount",
            name="comments",
        ),
        migrations.AddField(
            model_name="comments",
            name="discounts",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="catalog.discount",
            ),
        ),
    ]
