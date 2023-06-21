# Generated by Django 3.1.2 on 2020-10-17 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=8)),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='token',
            name='device_code',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
