# Generated by Django 3.1.5 on 2021-01-14 21:13
import pkgutil

import django.contrib.postgres.fields
from django.db import connection
from django.db import migrations
from django.db import models


def add_gcp_compute_views(apps, schema_editor):
    """Create the GCP Materialized views from files."""

    for view in ("", "_by_project", "_by_account", "_by_service", "_by_region"):
        view_sql = pkgutil.get_data("reporting.provider.gcp", f"sql/views/reporting_gcp_compute_summary{view}.sql")
        view_sql = view_sql.decode("utf-8")
        with connection.cursor() as cursor:
            cursor.execute(view_sql)


class Migration(migrations.Migration):

    dependencies = [("reporting", "0159_gcp_cost_summary")]

    operations = [migrations.RunPython(add_gcp_compute_views)]
