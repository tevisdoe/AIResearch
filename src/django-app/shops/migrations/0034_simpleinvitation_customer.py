# Generated by Django 4.1.2 on 2024-01-31 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_employeedata_shop"),
        ("shops", "0033_rename_simpleinviatation_simpleinvitation"),
    ]

    operations = [
        migrations.AddField(
            model_name="simpleinvitation",
            name="customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.customer",
            ),
        ),
    ]