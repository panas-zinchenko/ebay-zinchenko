# Generated by Django 3.2.8 on 2021-10-30 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_alter_lot_lot_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='LotCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=64)),
            ],
        ),
    ]