# Generated by Django 5.0.2 on 2024-04-30 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KitchenOwner', '0005_kitchen_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchen',
            name='city',
            field=models.CharField(choices=[('Riyadh', 'Riyadh'), ('Jeddah', 'Jeddah'), ('Dammam', 'Dammam')], max_length=100),
        ),
    ]