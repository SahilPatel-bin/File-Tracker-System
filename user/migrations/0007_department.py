# Generated by Django 4.1.7 on 2023-04-18 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=50)),
                ('scode', models.CharField(max_length=10)),
                ('cddept', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Department_Master',
            },
        ),
    ]
