# Generated by Django 4.1.7 on 2023-05-20 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0030_file_create_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='last_update_user_id',
            field=models.IntegerField(default='0', null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='receive_user_id',
            field=models.IntegerField(default='0', null=True),
        ),
    ]