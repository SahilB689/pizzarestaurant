# Generated by Django 2.2.10 on 2020-05-27 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0033_auto_20200527_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='menu_item',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='menu_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Menu_Item'),
        ),
    ]
