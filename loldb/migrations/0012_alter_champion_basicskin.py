# Generated by Django 4.0.4 on 2022-05-30 16:41

from django.db import migrations, models
import loldb.models


class Migration(migrations.Migration):

    dependencies = [
        ('loldb', '0011_alter_ability_options_champion_basicskin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champion',
            name='basicSkin',
            field=models.ImageField(blank=True, null=True, upload_to=loldb.models.champion_path, verbose_name='Basic skin'),
        ),
    ]
