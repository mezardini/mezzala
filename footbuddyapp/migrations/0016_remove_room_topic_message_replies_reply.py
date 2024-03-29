# Generated by Django 4.0.4 on 2022-04-27 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('footbuddyapp', '0015_remove_message_replies_delete_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='topic',
        ),
        migrations.AddField(
            model_name='message',
            name='replies',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='footbuddyapp.message')),
                ('replier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='footbuddyapp.room')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
