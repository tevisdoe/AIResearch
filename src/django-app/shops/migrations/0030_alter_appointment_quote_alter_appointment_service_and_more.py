# Generated by Django 4.1.2 on 2023-03-26 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0012_merge_20230317_1930"),
        ("vehicles", "0004_alter_vehicle_year"),
        ("shops", "0029_remove_workorder_quote_appointment_service_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="quote",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="quotes.quote",
            ),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="service",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="shops.service",
            ),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="vehicle",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="vehicles.vehicle",
            ),
        ),
    ]
