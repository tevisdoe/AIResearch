# Generated by Django 4.1.2 on 2024-01-31 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shops", "0032_simpleinviatation"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="SimpleInviatation",
            new_name="SimpleInvitation",
        ),
    ]