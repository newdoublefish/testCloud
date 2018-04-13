# Generated by Django 2.0.3 on 2018-04-12 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0005_auto_20180327_0003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='testtype',
            new_name='test_type',
        ),
        migrations.RemoveField(
            model_name='record',
            name='result_bool',
        ),
        migrations.AddField(
            model_name='record',
            name='result_integer',
            field=models.IntegerField(default=100, verbose_name='测试结果'),
        ),
    ]
