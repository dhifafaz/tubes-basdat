# Generated by Django 3.2 on 2021-05-07 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_api', '0031_alter_meminjam_tanggal_pengembalian'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meminjam',
            name='id_peminjam',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='library_api.peminjam'),
        ),
        migrations.AlterField(
            model_name='meminjam',
            name='isbn',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='library_api.buku'),
        ),
        migrations.AlterField(
            model_name='meminjam',
            name='tanggal_peminjaman',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='meminjam',
            name='tanggal_pengembalian',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='mengurusi',
            name='jenis',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='peminjam',
            name='tipe',
            field=models.CharField(max_length=10),
        ),
    ]
