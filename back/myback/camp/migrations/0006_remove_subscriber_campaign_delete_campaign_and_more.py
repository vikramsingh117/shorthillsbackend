# Generated by Django 4.0 on 2023-11-16 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0005_product_public_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='campaign',
        ),
        migrations.DeleteModel(
            name='Campaign',
        ),
        migrations.DeleteModel(
            name='Subscriber',
        ),
    ]
