# Generated by Django 2.1.5 on 2019-02-09 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpiderBT_Cases', '0003_auto_20190208_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='identifier',
            field=models.CharField(default='empty', max_length=200, verbose_name='ID of this Case'),
            preserve_default=False,
        ),
    ]