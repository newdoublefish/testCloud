# Generated by Django 2.0.3 on 2018-03-23 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_text', models.CharField(max_length=100, unique=True, verbose_name='控制盒编号')),
                ('dcd_text', models.CharField(max_length=50, verbose_name='绝缘检测板编号')),
                ('dcm_text', models.CharField(max_length=100, verbose_name='K60板编号')),
                ('pwr_text', models.CharField(max_length=50, verbose_name='电源板编号')),
                ('cpu_text', models.CharField(max_length=50, verbose_name='K64板编号')),
                ('g4_text', models.CharField(max_length=50, verbose_name='4G编号')),
                ('ddb_text', models.CharField(max_length=50, verbose_name='背板编号')),
                ('dcr_text', models.CharField(max_length=50, verbose_name='继电器板编号')),
                ('led_text', models.CharField(max_length=50, verbose_name='显示板编号')),
            ],
        ),
        migrations.AlterField(
            model_name='stubinfo',
            name='ammeter1_text',
            field=models.CharField(max_length=50, verbose_name='电表1'),
        ),
        migrations.AlterField(
            model_name='stubinfo',
            name='ammeter2_text',
            field=models.CharField(max_length=50, verbose_name='电表2'),
        ),
        migrations.AlterField(
            model_name='stubinfo',
            name='board_text',
            field=models.CharField(max_length=50, verbose_name='控制盒编号'),
        ),
        migrations.AlterField(
            model_name='stubinfo',
            name='gun1_text',
            field=models.CharField(max_length=50, verbose_name='枪1二维码'),
        ),
        migrations.AlterField(
            model_name='stubinfo',
            name='gun2_text',
            field=models.CharField(max_length=50, verbose_name='枪2二维码'),
        ),
        migrations.AlterField(
            model_name='stubinfo',
            name='gun_vendor_text',
            field=models.CharField(max_length=100, verbose_name='枪厂家'),
        ),
        migrations.AlterField(
            model_name='stubinfo',
            name='sim_text',
            field=models.CharField(max_length=100, verbose_name='sim卡号'),
        ),
        migrations.AlterField(
            model_name='stubinfo',
            name='stub_text',
            field=models.CharField(max_length=50, unique=True, verbose_name='铭牌编号'),
        ),
    ]
