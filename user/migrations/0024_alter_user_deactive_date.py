# Generated by Django 4.1.7 on 2023-04-26 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_alter_user_circle_code_alter_user_department_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='deactive_date',
            field=models.DateTimeField(default=0, null=True),
        ),
    ]
