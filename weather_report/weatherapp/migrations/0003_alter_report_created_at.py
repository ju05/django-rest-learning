# Generated by Django 4.2.2 on 2023-06-17 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0002_alter_report_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
