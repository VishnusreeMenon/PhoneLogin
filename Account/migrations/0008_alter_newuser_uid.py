# Generated by Django 3.2.5 on 2022-12-07 17:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0007_alter_newuser_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('a2f306a1-a081-47d7-8a9f-37ddc8583eb9')),
        ),
    ]
