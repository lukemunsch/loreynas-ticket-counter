# Generated by Django 3.2 on 2022-04-22 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0003_auto_20220422_1212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='district',
            old_name='area_name',
            new_name='area',
        ),
    ]