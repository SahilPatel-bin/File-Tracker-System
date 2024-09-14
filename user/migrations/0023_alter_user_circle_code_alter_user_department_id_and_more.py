# Generated by Django 4.1.7 on 2023-04-26 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_alter_user_cdeptid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='circle_code',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='user',
            name='department_id',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='user',
            name='design_id',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='user',
            name='division_code',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='user',
            name='office_code',
            field=models.IntegerField(default='5'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(default='0', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role_id',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='user',
            name='subdivision_code',
            field=models.IntegerField(default='0'),
        ),
    ]