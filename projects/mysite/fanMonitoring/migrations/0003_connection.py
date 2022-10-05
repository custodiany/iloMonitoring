# Generated by Django 4.1.1 on 2022-10-03 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fanMonitoring', '0002_ilo_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connectToLinux', models.BooleanField()),
                ('connectToIlo', models.BooleanField()),
                ('serverId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fanMonitoring.server')),
            ],
        ),
    ]