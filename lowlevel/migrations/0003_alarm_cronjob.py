# Generated by Django 2.1.4 on 2018-12-30 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("lowlevel", "0002_auto_20181230_1723")]

    operations = [
        migrations.AddField(
            model_name="alarm",
            name="cronjob",
            field=models.CharField(default="none", max_length=36),
            preserve_default=False,
        )
    ]
