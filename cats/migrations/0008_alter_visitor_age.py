# Generated by Django 4.1.7 on 2023-06-07 21:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cats", "0007_alter_visitor_age_alter_visitor_cat_age"),
    ]

    operations = [
        migrations.AlterField(
            model_name="visitor",
            name="age",
            field=models.PositiveSmallIntegerField(),
        ),
    ]
