# Generated by Django 2.1.5 on 2019-02-08 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SpiderBT_Cases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SpiderBT_Cases.Category'),
        ),
    ]