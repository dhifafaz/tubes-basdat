# Generated by Django 3.2 on 2021-05-05 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_api', '0003_alter_buku_judul_buku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosen',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='peminjam',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
