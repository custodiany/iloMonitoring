# Generated by Django 4.1.1 on 2022-10-05 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanMonitoring', '0004_alter_connection_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmh',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ilo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='network',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]