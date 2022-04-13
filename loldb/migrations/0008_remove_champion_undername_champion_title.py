# Generated by Django 4.0.4 on 2022-04-13 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loldb', '0007_ability_championname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='champion',
            name='underName',
        ),
        migrations.AddField(
            model_name='champion',
            name='title',
            field=models.CharField(default=1, max_length=50, verbose_name='Title'),
            preserve_default=False,
        ),
    ]
