# Generated by Django 3.2.9 on 2021-11-03 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_alter_lot_lot_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='lot_bid',
            field=models.ForeignKey(default='have no bid yet', on_delete=django.db.models.deletion.CASCADE, related_name='lotbid', to='auctions.bid'),
        ),
    ]
