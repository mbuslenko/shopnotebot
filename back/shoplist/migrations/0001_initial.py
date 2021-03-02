# Generated by Django 3.1.7 on 2021-03-01 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.PositiveIntegerField(verbose_name="User's id")),
                ('name', models.TextField(verbose_name="User's name")),
            ],
            options={
                'verbose_name': 'Profile',
            },
        ),
    ]