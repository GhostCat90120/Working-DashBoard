# Generated by Django 4.1.3 on 2023-11-29 06:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project_apps", "0002_alter_inventory_month"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="inventory",
            name="customers",
        ),
        migrations.AlterField(
            model_name="inventory",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
