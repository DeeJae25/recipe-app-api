# Generated by Django 3.2.23 on 2023-11-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20231123_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]