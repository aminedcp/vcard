# Generated by Django 4.0.5 on 2022-07-20 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0005_informationvcard_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informationvcard',
            name='telephonepro1',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Tél 1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='informationvcard',
            name='telephonepro2',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Tél 2'),
            preserve_default=False,
        ),
    ]
