# Generated by Django 4.2.6 on 2023-10-09 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
