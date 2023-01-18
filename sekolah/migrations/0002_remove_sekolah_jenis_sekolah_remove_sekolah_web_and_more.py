# Generated by Django 4.1.5 on 2023-01-18 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sekolah', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sekolah',
            name='jenis_sekolah',
        ),
        migrations.RemoveField(
            model_name='sekolah',
            name='web',
        ),
        migrations.AddField(
            model_name='sekolah',
            name='kabupaten_kota',
            field=models.TextField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='sekolah',
            name='npsn',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='sekolah',
            name='provinsi',
            field=models.TextField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='sekolah',
            name='status',
            field=models.CharField(choices=[('Swasta', 'Swasta'), ('Negeri', 'Negeri')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='sekolah',
            name='alamat',
            field=models.TextField(blank=True, max_length=254, null=True),
        ),
    ]