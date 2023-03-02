# Generated by Django 4.1.3 on 2023-02-28 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfEnvir',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('position', models.SmallIntegerField(default=1, verbose_name='排序')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='名称')),
            ],
            options={
                'verbose_name': '环境配置字典表',
                'db_table': 'conf_envir',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='ConfParamType',
            fields=[
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('position', models.SmallIntegerField(default=1, verbose_name='排序')),
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': '参数类型表',
                'db_table': 'conf_param_type',
                'ordering': ('position',),
            },
        ),
    ]
