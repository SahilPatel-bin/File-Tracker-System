# Generated by Django 4.1.7 on 2023-04-19 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_office'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'Role_Master',
            },
        ),
    ]