# Generated by Django 3.2.5 on 2022-12-07 17:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('69a0f6f6-6c5a-4b02-ad8b-7b48f3be7e4b')),
        ),
    ]
