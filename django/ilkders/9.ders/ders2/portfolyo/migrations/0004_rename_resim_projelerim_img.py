# Generated by Django 5.0 on 2023-12-19 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolyo', '0003_alter_projelerim_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projelerim',
            old_name='resim',
            new_name='img',
        ),
    ]
