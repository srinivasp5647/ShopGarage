# Generated by Django 3.1.3 on 2020-11-29 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CartItems',
            new_name='CartItem',
        ),
    ]