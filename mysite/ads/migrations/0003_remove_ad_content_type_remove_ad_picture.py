# Generated by Django 4.2.7 on 2024-04-10 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0002_ad_content_type_ad_picture"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ad",
            name="content_type",
        ),
        migrations.RemoveField(
            model_name="ad",
            name="picture",
        ),
    ]