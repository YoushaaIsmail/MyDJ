# Generated by Django 4.2.6 on 2023-11-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_alter_billing_type_address_alter_order_name_prod_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='type_address',
            field=models.CharField(choices=[('Apartment', 'Apartment'), ('Home', 'Home'), ('office', 'office')], max_length=100, verbose_name='type_address:'),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='listt',
            field=models.CharField(choices=[('discount', 'خصومات'), ('Black', 'أسود'), ('ALHajab', 'ALHajab'), ('winter', 'قطع شتوية'), ('classic', 'عصري(كلاسيكي)'), ('New', 'جديد'), ('Summer', 'قطع صيفية')], max_length=100, verbose_name='تصنيف المنتج '),
        ),
    ]