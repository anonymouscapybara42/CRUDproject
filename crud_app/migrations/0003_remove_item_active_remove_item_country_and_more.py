# Generated by Django 5.2.1 on 2025-05-19 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0002_item_active_item_country_item_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='active',
        ),
        migrations.RemoveField(
            model_name='item',
            name='country',
        ),
        migrations.RemoveField(
            model_name='item',
            name='role',
        ),
        migrations.AddField(
            model_name='item',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
