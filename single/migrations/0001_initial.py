# Generated by Django 3.2.2 on 2021-05-10 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Single',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('youtube_view', models.IntegerField()),
            ],
            options={
                'db_table': 'single',
            },
        ),
    ]