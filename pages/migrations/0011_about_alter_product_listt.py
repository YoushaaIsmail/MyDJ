# Generated by Django 4.2.6 on 2023-11-03 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_alter_order_note_alter_order_width_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField(verbose_name='وصف الخدمات ')),
                ('imgprofile', models.ImageField(upload_to=None, verbose_name='الصورة الرئيسية')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='listt',
            field=models.CharField(choices=[('Black', 'Black'), ('New', 'New'), ('Summer', 'Summer'), ('classic', 'classic'), ('sold', 'sold'), ('ALHajab', 'ALHajab'), ('winter', 'winter')], max_length=100, verbose_name='list:'),
        ),
    ]