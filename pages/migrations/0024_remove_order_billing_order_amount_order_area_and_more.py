# Generated by Django 4.2.6 on 2023-11-07 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_alter_billing_type_address_alter_order_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='billing',
        ),
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=1, verbose_name='amount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='area',
            field=models.CharField(default=1, max_length=500, verbose_name='Area'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='block',
            field=models.CharField(default=1, max_length=500, verbose_name='Block'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='house',
            field=models.CharField(default=1, max_length=500, verbose_name='house'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.BooleanField(default=False, verbose_name='payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='street',
            field=models.CharField(default=1, max_length=500, verbose_name='street'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='type_address',
            field=models.CharField(choices=[('office', 'office'), ('Home', 'Home'), ('Apartment', 'Apartment')], default=1, max_length=100, verbose_name='type_address:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='listt',
            field=models.CharField(choices=[('classic', 'عصري(كلاسيكي)'), ('ALHajab', 'ALHajab'), ('winter', 'قطع شتوية'), ('Black', 'أسود'), ('discount', 'خصومات'), ('New', 'جديد'), ('Summer', 'قطع صيفية')], max_length=100, verbose_name='تصنيف المنتج '),
        ),
        migrations.DeleteModel(
            name='billing',
        ),
    ]