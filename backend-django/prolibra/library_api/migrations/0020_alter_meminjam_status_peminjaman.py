# Generated by Django 3.2 on 2021-05-05 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_api', '0019_alter_meminjam_status_peminjaman'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meminjam',
            name='status_peminjaman',
            field=models.CharField(default='Belum dikembalikan', max_length=255, null=True),
        ),
    ]
