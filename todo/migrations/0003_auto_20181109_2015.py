# Generated by Django 2.1.3 on 2018-11-09 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20181109_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitem',
            old_name='text',
            new_name='item',
        ),
    ]
