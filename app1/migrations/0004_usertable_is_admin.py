# Generated by Django 4.0.6 on 2022-07-14 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_usertable_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertable',
            name='is_admin',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]