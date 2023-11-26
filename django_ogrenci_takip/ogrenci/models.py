from django.db import models


# Create your models here.

class Kulupler(models.Model):
    kulupAd = models.CharField(max_length=50)
    kulupKontenjan = models.IntegerField()

    def __str__(self):
        return self.kulupAd


class Dersler(models.Model):
    dersAd = models.CharField(max_length=50)

    def __str__(self):
        return self.dersAd


class Ogrenciler(models.Model):
    ogrenciAd = models.CharField(max_length=30)
    ogrenciSoyad = models.CharField(max_length=30)
    ogrenciFotograf = models.CharField(max_length=255, null=True, blank=True)
    cinsiyet = [
        ('E', 'Erkek'),
        ('K', 'Kadın'),
    ]
    ogrenciCinsiyet = models.CharField(max_length=1, choices=cinsiyet)
    ogrenciKulup = models.ForeignKey(Kulupler, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.ogrenciAd


class Notlar(models.Model):
    dersId = models.ManyToManyField(Dersler)
    ogrenciId = models.ManyToManyField(Ogrenciler)
    sinav1 = models.CharField(max_length=3)
    sinav2 = models.CharField(max_length=3)
    sinav3 = models.CharField(max_length=3)
    proje = models.CharField(max_length=3)
    ortalama = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    durum = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.ogrenciId.values_list('ogrenciAd', flat=True)[0]}" \
               f" {self.ogrenciId.values_list('ogrenciSoyad', flat=True)[0]}" \
               f" {self.dersId.values_list('dersAd', flat=True)[0]}"

    def hesapla(self):
        ortalamaHesapla = (int(self.sinav1) + int(self.sinav2) + int(self.sinav3) + int(self.proje)) / 4
        self.ortalama = ortalamaHesapla
        if ortalamaHesapla >= 50:
            self.durum = True

    def save(self, *args, **kwargs):
        self.hesapla()
        super().save(*args, **kwargs)


