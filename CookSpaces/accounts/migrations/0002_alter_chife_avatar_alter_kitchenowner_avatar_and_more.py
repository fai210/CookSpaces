# Generated by Django 5.0.4 on 2024-04-24 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chife',
            name='avatar',
            field=models.FileField(default='images/default.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='kitchenowner',
            name='avatar',
            field=models.FileField(default='images/default.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='renter',
            name='avatar',
            field=models.FileField(default='images/default.jpg', upload_to='images/'),
        ),
    ]