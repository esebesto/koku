# Generated by Django 2.1.5 on 2019-02-08 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0029_auto_20190207_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='ocpawscostlineitemdailysummary',
            name='normalized_usage_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='ocpawscostlineitemdailysummary',
            name='usage_amount',
            field=models.FloatField(null=True),
        ),
    ]