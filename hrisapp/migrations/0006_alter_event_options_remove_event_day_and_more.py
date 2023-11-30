# Generated by Django 4.2.7 on 2023-11-28 20:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hrisapp", "0005_event"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="event",
            options={},
        ),
        migrations.RemoveField(
            model_name="event",
            name="day",
        ),
        migrations.RemoveField(
            model_name="event",
            name="notes",
        ),
        migrations.AddField(
            model_name="event",
            name="description",
            field=models.TextField(default=" ", editable=False, max_length=600),
        ),
        migrations.AddField(
            model_name="event",
            name="title",
            field=models.CharField(default=" ", editable=False, max_length=200),
        ),
        migrations.AlterField(
            model_name="event",
            name="end_time",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="event",
            name="start_time",
            field=models.DateTimeField(),
        ),
    ]