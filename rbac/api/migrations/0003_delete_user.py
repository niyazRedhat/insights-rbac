# Generated by Django 2.2.4 on 2020-04-08 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("api", "0002_remove_user_email")]

    operations = [migrations.DeleteModel(name="User")]
