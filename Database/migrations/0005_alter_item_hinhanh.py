# Generated by Django 3.2.8 on 2021-11-30 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0004_alter_item_hinhanh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='hinhAnh',
            field=models.TextField(),
        ),
    ]