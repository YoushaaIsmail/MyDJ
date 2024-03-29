# Generated by Django 4.2.6 on 2023-11-06 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_product_url_alter_billing_type_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='type_address',
            field=models.CharField(choices=[('office', 'office'), ('Home', 'Home'), ('Apartment', 'Apartment')], max_length=100, verbose_name='type_address:'),
        ),
        migrations.AlterField(
            model_name='order',
            name='name_prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.product', verbose_name='اسم القطعة المطلوبة'),
        ),
        migrations.AlterField(
            model_name='product',
            name='listt',
            field=models.CharField(choices=[('discount', 'خصومات'), ('winter', 'قطع شتوية'), ('New', 'جديد'), ('Black', 'أسود'), ('Summer', 'قطع صيفية'), ('classic', 'عصري(كلاسيكي)'), ('ALHajab', 'ALHajab')], max_length=100, verbose_name='تصنيف المنتج '),
        ),
    ]
