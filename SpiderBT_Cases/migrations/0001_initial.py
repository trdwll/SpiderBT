# Generated by Django 2.1.5 on 2019-02-08 23:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SpiderBT_Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='The creation date of the case.')),
                ('date_updated', models.DateTimeField(blank=True, help_text='The date that the case was updated.', null=True)),
                ('date_solved', models.DateTimeField(blank=True, help_text='The date that the case was solved.', null=True)),
                ('title', models.CharField(help_text='Why are you submitting a report today?', max_length=120)),
                ('body', models.TextField(blank=True, help_text='Explain why are you submitting a report today?')),
                ('visibility', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='public', max_length=120)),
                ('severity', models.CharField(choices=[('urgent', 'Urgent'), ('critical', 'Critical'), ('major', 'Major'), ('minor', 'Minor'), ('low', 'Low'), ('verylow', 'Very Low')], default='minor', max_length=120)),
                ('status', models.CharField(choices=[('open', 'Open'), ('inprogress', 'In Progress'), ('onhold', 'On Hold'), ('closed', 'Closed')], default='open', max_length=120)),
                ('reproducibility', models.CharField(choices=[('always', 'Always'), ('sometimes', 'Sometimes'), ('random', 'Random'), ('havenottried', 'Have Not Tried'), ('unable', 'Unable to Reproduce'), ('na', 'N/A')], default='havenottried', max_length=120)),
                ('patch_commit', models.CharField(blank=True, help_text='What is the commit ID that this Case was fixed on?', max_length=120, verbose_name='Patched Commit')),
            ],
        ),
        migrations.CreateModel(
            name='CaseNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(help_text='Explain why are you submitting a report today?')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='The creation date of the case note.')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SpiderBT_Cases.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the category.', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the product.', max_length=120)),
                ('description', models.TextField()),
                ('abbreviation', models.CharField(help_text='A simple identifier to reference cases.', max_length=10)),
                ('visibility', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='public', max_length=120)),
                ('date', models.DateTimeField(auto_now_add=True, help_text='The creation date of the product.')),
                ('slug', models.SlugField(unique=True)),
                ('usergroups', models.ManyToManyField(blank=True, help_text='What usergroups are able to access this product?', related_name='usergroups', to='SpiderBT_Users.UserGroup')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the product version.', max_length=120)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SpiderBT_Cases.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('case', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SpiderBT_Cases.Case')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SpiderBT_Cases.Product'),
        ),
        migrations.AddField(
            model_name='case',
            name='affect_version',
            field=models.ManyToManyField(blank=True, help_text='What version(s) of the product does this affect (your current version)?', related_name='affect_version', to='SpiderBT_Cases.ProductVersion', verbose_name='Affected Version(s)'),
        ),
        migrations.AddField(
            model_name='case',
            name='assigned_to_group',
            field=models.ManyToManyField(blank=True, related_name='assigned_to_group', to='SpiderBT_Users.UserGroup'),
        ),
        migrations.AddField(
            model_name='case',
            name='assigned_to_user',
            field=models.ManyToManyField(blank=True, related_name='assigned_to_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='case',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='case',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='SpiderBT_Cases.Category'),
        ),
        migrations.AddField(
            model_name='case',
            name='patch_version',
            field=models.ForeignKey(blank=True, help_text='What version of the product will this fix be pushed out?', on_delete=django.db.models.deletion.CASCADE, related_name='patch_version', to='SpiderBT_Cases.ProductVersion', verbose_name='Patched Version'),
        ),
        migrations.AddField(
            model_name='case',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SpiderBT_Cases.Product'),
        ),
    ]
