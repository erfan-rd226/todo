# Generated by Django 4.2.4 on 2023-08-12 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_todo_user_todo_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='users',
            new_name='user',
        ),
    ]
