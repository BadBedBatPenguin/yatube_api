# Generated by Django 2.2.16 on 2022-01-23 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20220116_1741'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pub_date',)},
        ),
    ]