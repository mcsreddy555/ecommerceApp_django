# Generated by Django 3.1.2 on 2020-10-22 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_showdetails_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='showDetails',
        ),
        migrations.AddField(
            model_name='product',
            name='details',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manifactDetls',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='package',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='warranty',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Showdetails',
        ),
    ]
