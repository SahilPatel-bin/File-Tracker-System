# Generated by Django 4.1.7 on 2023-04-19 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_division'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_code', models.IntegerField(default=0)),
                ('office_name', models.CharField(max_length=50)),
                ('office_contact', models.CharField(max_length=50)),
                ('uadserver', models.CharField(max_length=30)),
                ('udn', models.CharField(max_length=50)),
                ('uldaprdn', models.CharField(max_length=20)),
                ('display_entry', models.IntegerField(default=0)),
                ('short_code', models.CharField(max_length=3)),
                ('cr_short_code', models.CharField(max_length=7)),
            ],
            options={
                'db_table': 'Office_Master',
            },
        ),
    ]