# Generated by Django 3.2.5 on 2021-08-04 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_telegram_bot_django_persistence', '0002_alter_conversationdata_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='user_id',
            field=models.BigIntegerField(),
        ),
    ]
