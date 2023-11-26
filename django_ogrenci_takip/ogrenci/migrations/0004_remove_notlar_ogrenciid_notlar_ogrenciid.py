# Generated by Django 4.2.6 on 2023-11-11 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ogrenci', '0003_alter_notlar_ortalama_alter_ogrenciler_ogrencikulup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notlar',
            name='ogrenciId',
        ),
        migrations.AddField(
            model_name='notlar',
            name='ogrenciId',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='ogrenci.ogrenciler'),
            preserve_default=False,
        ),
    ]
