# Generated by Django 4.0.5 on 2022-07-13 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informationvcard',
            name='telephonepoerso3',
        ),
        migrations.AddField(
            model_name='informationvcard',
            name='telephonepro1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tél 1'),
        ),
        migrations.AddField(
            model_name='informationvcard',
            name='telephonepro2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tél 2'),
        ),
        migrations.AlterField(
            model_name='informationvcard',
            name='Adressepro',
            field=models.TextField(blank=True, null=True, verbose_name='Organisme'),
        ),
        migrations.AlterField(
            model_name='informationvcard',
            name='cv_recto',
            field=models.FileField(upload_to='files', verbose_name='Recto'),
        ),
        migrations.AlterField(
            model_name='informationvcard',
            name='cv_verso',
            field=models.FileField(blank=True, null=True, upload_to='files', verbose_name='Verso'),
        ),
        migrations.AlterField(
            model_name='informationvcard',
            name='emailorganisme1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Organisme'),
        ),
        migrations.AlterField(
            model_name='informationvcard',
            name='emailorganisme2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Organisme'),
        ),
        migrations.AlterField(
            model_name='informationvcard',
            name='emailperso',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Organisme'),
        ),
        migrations.AlterField(
            model_name='informationvcard',
            name='fax',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Organisme'),
        ),
        migrations.AlterField(
            model_name='informationvcard',
            name='nom',
            field=models.CharField(max_length=100, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='informationvcard',
            name='nomar',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nom en arabe'),
        ),
        migrations.AlterField(
            model_name='informationvcard',
            name='prenom',
            field=models.CharField(max_length=100, verbose_name='Prénom'),
        ),
        migrations.AlterField(
            model_name='informationvcard',
            name='prenomar',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Prénom en arabe'),
        ),
        migrations.AlterField(
            model_name='informationvcard',
            name='telephoneperso1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tél 1'),
        ),
        migrations.AlterField(
            model_name='informationvcard',
            name='telephoneperso2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tél 2'),
        ),
    ]