# Generated by Django 2.1.5 on 2019-02-21 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SpiderBT_Cases', '0008_auto_20190210_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casevote',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SpiderBT_Cases.Case'),
        ),
    ]