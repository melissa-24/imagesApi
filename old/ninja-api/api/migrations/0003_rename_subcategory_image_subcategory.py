# Generated by Django 4.2.6 on 2023-10-23 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_imagelink_extension_uploadimage_extension'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='SubCategory',
            new_name='subCategory',
        ),
    ]
