# Generated by Django 4.1.2 on 2023-01-02 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shops", "0017_remove_appointmentslot_booked_slots_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointmentslot",
            name="appointment",
            field=models.ManyToManyField(blank=True, to="shops.appointment"),
        ),
    ]