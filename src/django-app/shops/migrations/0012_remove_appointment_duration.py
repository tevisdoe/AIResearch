# Generated by Django 4.1.2 on 2022-11-29 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shops", "0011_appointment_service_workorder_servicepart_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="appointment",
            name="duration",
        ),
    ]
