# Generated by Django 4.2.7 on 2023-12-03 20:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("hrisapp", "0011_alter_event_from"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="From",
        ),
    ]