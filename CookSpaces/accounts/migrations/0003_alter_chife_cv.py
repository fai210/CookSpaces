# Generated by Django 5.0.4 on 2024-04-30 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_chife_avatar_alter_kitchenowner_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chife',
            name='cv',
            field=models.FileField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
