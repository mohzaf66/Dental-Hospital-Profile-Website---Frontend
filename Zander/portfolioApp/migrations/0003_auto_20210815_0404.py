# Generated by Django 2.2.14 on 2021-08-15 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0002_auto_20210705_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='Question',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='Post',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.RemoveField(
            model_name='querie',
            name='user',
        ),
        migrations.DeleteModel(
            name='Website',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Querie',
        ),
    ]
