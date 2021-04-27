# Generated by Django 3.2 on 2021-04-25 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.product'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]