# Generated by Django 4.1.5 on 2023-02-06 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datarepo', '0006_remove_product_datarepo_pr_name_e6d26a_idx'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name'], name='datarepo_pr_name_e6d26a_idx'),
        ),
    ]
