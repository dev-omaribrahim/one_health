# Generated by Django 4.2 on 2024-07-09 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0002_alter_category_slug"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["name"],
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
    ]