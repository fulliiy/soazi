# Generated by Django 2.0.6 on 2018-07-03 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PushLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.ArticleList', verbose_name='文章')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
            options={
                'verbose_name': '操作记录',
                'verbose_name_plural': '操作记录',
                'db_table': 'pushlog',
            },
        ),
    ]
