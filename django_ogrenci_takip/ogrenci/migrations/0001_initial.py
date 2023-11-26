# Generated by Django 4.2.6 on 2023-10-21 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dersler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dersAd', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Kulupler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kulupAd', models.CharField(max_length=50)),
                ('kulupKontenjan', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ogrenciler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ogrenciAd', models.CharField(max_length=30)),
                ('ogrenciSoyad', models.CharField(max_length=30)),
                ('ogrenciFotograf', models.CharField(blank=True, max_length=255, null=True)),
                ('ogrenciCinsiyet', models.CharField(choices=[('E', 'Erkek'), ('K', 'Kadın')], max_length=1)),
                ('ogrenciKulup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ogrenci.kulupler')),
            ],
        ),
        migrations.CreateModel(
            name='Notlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sinav1', models.CharField(max_length=3)),
                ('sinav2', models.CharField(max_length=3)),
                ('sinav3', models.CharField(max_length=3)),
                ('proje', models.CharField(max_length=3)),
                ('ortalama', models.DecimalField(decimal_places=2, max_digits=3)),
                ('durum', models.BooleanField(default=False)),
                ('dersId', models.ManyToManyField(to='ogrenci.dersler')),
                ('ogrenciId', models.ManyToManyField(to='ogrenci.ogrenciler')),
            ],
        ),
    ]
