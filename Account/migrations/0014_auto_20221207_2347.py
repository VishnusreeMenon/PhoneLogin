# Generated by Django 3.2.5 on 2022-12-07 18:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0013_alter_newuser_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('6a45d696-c7ef-4cd9-a601-27965a7aba68')),
        ),
        migrations.AlterField(
            model_name='profile',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Account.newuser'),
        ),
    ]
