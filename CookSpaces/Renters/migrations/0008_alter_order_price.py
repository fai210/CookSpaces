# Generated by Django 5.0.4 on 2024-04-30 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Renters', '0007_merge_20240430_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]