# Generated by Django 5.1.3 on 2024-11-25 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0009_uploadfiles_alter_auto_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
