# Generated by Django 3.0.5 on 2022-04-19 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Admin'), (2, 'Manager'), (3, 'Employee')], default=1, null=True),
        ),
    ]
