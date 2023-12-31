# Generated by Django 3.2.5 on 2021-07-19 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='BotData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namespace', models.CharField(blank=True, max_length=255)),
                ('data', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CallbackData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namespace', models.CharField(blank=True, max_length=255)),
                ('data', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChatData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namespace', models.CharField(blank=True, max_length=255)),
                ('chat_id', models.BigIntegerField()),
                ('data', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='ConversationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namespace', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('key', models.TextField()),
                ('state', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namespace', models.CharField(blank=True, max_length=255)),
                ('user_id', models.BigIntegerField(unique=True)),
                ('data', models.JSONField()),
            ],
        ),
        migrations.AddIndex(
            model_name='userdata',
            index=models.Index(fields=['namespace', 'user_id'], name='python_tele_namespa_3c44b8_idx'),
        ),
        migrations.AddConstraint(
            model_name='userdata',
            constraint=models.UniqueConstraint(fields=('namespace', 'user_id'), name='unique_user_id'),
        ),
        migrations.AddIndex(
            model_name='conversationdata',
            index=models.Index(fields=['namespace', 'name', 'key'], name='python_tele_namespa_1b4da9_idx'),
        ),
        migrations.AddConstraint(
            model_name='conversationdata',
            constraint=models.UniqueConstraint(fields=('namespace', 'name', 'key'), name='unique_conversation_data'),
        ),
        migrations.AddIndex(
            model_name='chatdata',
            index=models.Index(fields=['namespace', 'chat_id'], name='python_tele_namespa_31f032_idx'),
        ),
        migrations.AddConstraint(
            model_name='chatdata',
            constraint=models.UniqueConstraint(fields=('namespace', 'chat_id'), name='unique_chat_id'),
        ),
    ]
