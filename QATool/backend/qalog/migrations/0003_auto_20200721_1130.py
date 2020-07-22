# Generated by Django 3.0.7 on 2020-07-21 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qalog', '0002_auto_20200720_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qalog',
            name='QALogID',
        ),
        migrations.AddField(
            model_name='qalog',
            name='DevelopedBy',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='qalog',
            name='ObjectName',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='qalog',
            name='ObjectPath',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='qalog',
            name='JIRALogFlag',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='qalog',
            name='QAConnID',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='qalog',
            name='QACreatedDate',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='qalog',
            name='QALog',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
        migrations.AlterField(
            model_name='qalog',
            name='QALoggedDate',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='qalog',
            name='SystemType',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]