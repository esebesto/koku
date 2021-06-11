# Generated by Django 3.1.10 on 2021-05-14 17:53
import os
import sys

from django.db import migrations

from koku import migration_sql_helpers as msh


def apply_public_function_updates(apps, schema_editor):
    path = msh.find_db_functions_dir()
    for funcfile in ("jsonb_sha256_text.sql",):
        msh.apply_sql_file(schema_editor, os.path.join(path, funcfile))


class Migration(migrations.Migration):

    dependencies = [("api", "0045_update_django_migration_sequences")]

    operations = [migrations.RunPython(code=apply_public_function_updates)]