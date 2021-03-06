# Generated by Django 4.0.4 on 2022-05-14 20:24

from django.db import migrations, models
import loldb.models


class Migration(migrations.Migration):

    dependencies = [
        ('loldb', '0010_region_icon'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ability',
            options={'ordering': ['name'], 'verbose_name_plural': 'abilities'},
        ),
        migrations.AddField(
            model_name='champion',
            name='basicSkin',
            field=models.FileField(blank=True, null=True, upload_to=loldb.models.champion_path, verbose_name='Basic skin'),
        ),
        migrations.AlterField(
            model_name='region',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=loldb.models.region_icon, verbose_name='Icon'),
        ),
    ]
