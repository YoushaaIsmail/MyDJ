# Generated by Django 4.2.6 on 2023-11-06 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_alter_billing_type_address_alter_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='type_address',
            field=models.CharField(choices=[('office', 'office'), ('Apartment', 'Apartment'), ('Home', 'Home')], max_length=100, verbose_name='type_address:'),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='listt',
            field=models.CharField(choices=[('classic', 'عصري(كلاسيكي)'), ('Black', 'أسود'), ('New', 'جديد'), ('discount', 'خصومات'), ('winter', 'قطع شتوية'), ('Summer', 'قطع صيفية'), ('ALHajab', 'ALHajab')], max_length=100, verbose_name='تصنيف المنتج '),
        ),
    ]