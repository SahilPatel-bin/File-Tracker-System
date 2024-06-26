# Generated by Django 4.1.7 on 2023-04-19 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_id', models.IntegerField(default=0)),
                ('subdivision_code', models.IntegerField(default=0)),
                ('subdivision_name', models.CharField(max_length=50)),
                ('circle_code', models.IntegerField(default=0)),
                ('division_code', models.IntegerField(default=0)),
                ('subdivision_contact', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Subdividsion_Master',
            },
        ),
    ]
