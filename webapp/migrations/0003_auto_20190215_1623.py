# Generated by Django 2.1.7 on 2019-02-15 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20190215_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exchanges',
            old_name='exchnge_name',
            new_name='exchange_name',
        ),
    ]