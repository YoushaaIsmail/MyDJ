# Generated by Django 4.2.6 on 2023-11-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_order_id_alter_order_type_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='listt',
            field=models.CharField(choices=[('New', 'New'), ('classic', 'classic'), ('winter', 'winter'), ('sold', 'sold'), ('ALHajab', 'ALHajab'), ('Black', 'Black'), ('Summer', 'Summer')], max_length=100, verbose_name='list:'),
        ),
    ]
