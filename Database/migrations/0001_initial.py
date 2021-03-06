# Generated by Django 3.2.9 on 2021-11-25 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('maSP', models.AutoField(primary_key=True, serialize=False)),
                ('tenSP', models.CharField(max_length=20)),
                ('giaBan', models.FloatField()),
                ('hinhAnh', models.ImageField(upload_to='')),
                ('available', models.BooleanField()),
                ('moTa', models.TextField()),
                ('type', models.CharField(max_length=10)),
            ],
        ),
    ]
