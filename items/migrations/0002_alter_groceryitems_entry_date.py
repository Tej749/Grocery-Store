# Generated by Django 5.1.2 on 2024-11-04 11:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="groceryitems",
            name="entry_date",
            field=models.DateField(),
        ),
    ]
