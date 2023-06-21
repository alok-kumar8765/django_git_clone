# Generated by Django 3.0.7 on 2020-07-29 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_directory_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('following', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('description', models.TextField()),
                ('organization', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('website', models.URLField()),
                ('avatar', models.URLField()),
            ],
        ),
    ]
