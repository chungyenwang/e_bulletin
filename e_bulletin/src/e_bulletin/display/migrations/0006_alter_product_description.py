# Generated by Django 3.2.4 on 2021-06-14 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0005_auto_20210614_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
