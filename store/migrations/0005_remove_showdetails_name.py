# Generated by Django 3.1.2 on 2020-10-22 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_showdetails_package'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showdetails',
            name='name',
        ),
    ]
