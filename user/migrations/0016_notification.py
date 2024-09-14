# Generated by Django 4.1.7 on 2023-04-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_file_create_delete_file_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.IntegerField()),
                ('file_name', models.CharField(max_length=100)),
                ('sender_user_id', models.IntegerField(default='null', null=True)),
                ('sender_uname', models.CharField(default='null', max_length=50, null=True)),
                ('sender_date', models.DateTimeField()),
                ('receive_user_id', models.IntegerField(default='null', null=True)),
                ('receiver_uname', models.CharField(default='null', max_length=50, null=True)),
                ('action', models.CharField(default='null', max_length=20, null=True)),
                ('action_read_date', models.DateTimeField()),
                ('action_remarks', models.CharField(default='null', max_length=500, null=True)),
                ('action_date', models.DateTimeField()),
                ('last_update_user_id', models.IntegerField(default='null', null=True)),
                ('last_update_date', models.DateTimeField()),
                ('last_updated_ip', models.CharField(default='null', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Notification',
            },
        ),
    ]