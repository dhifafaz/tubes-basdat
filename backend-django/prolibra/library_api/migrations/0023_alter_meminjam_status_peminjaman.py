# Generated by Django 3.2 on 2021-05-05 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_api', '0022_alter_meminjam_status_peminjaman'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meminjam',
            name='status_peminjaman',
            field=models.CharField(default='Belum dikembalikan', max_length=100),
        ),
    ]
