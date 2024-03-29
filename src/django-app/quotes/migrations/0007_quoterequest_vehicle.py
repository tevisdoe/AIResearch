# Generated by Django 4.1.2 on 2023-02-02 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("vehicles", "0004_alter_vehicle_year"),
        ("quotes", "0006_quoterequest_preferred_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="quoterequest",
            name="vehicle",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="vehicles.vehicle",
            ),
        ),
    ]