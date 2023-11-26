from django import forms
from django.forms import widgets
from . import models


class KulupForm(forms.ModelForm):
    class Meta:
        model = models.Kulupler
        fields = [
            "kulupAd",
            "kulupKontenjan"
        ]

        labels = {
            'kulupAd': "Kulüp Adı",
            'kulupKontenjan': "Kulüp Kontenjanı",
        }

        widgets = {
            "kulupAd": widgets.TextInput(attrs={"class": "form-control"}),
            "kulupKontenjan": widgets.TextInput(attrs={"class": "form-control"})
        }


class OgrenciForm(forms.ModelForm):
    class Meta:
        model = models.Ogrenciler
        fields = [
            "ogrenciAd",
            "ogrenciSoyad",
            "ogrenciCinsiyet",
            "ogrenciKulup"
        ]

        labels = {
            "ogrenciAd": "Öğrenci Adı",
            "ogrenciSoyad": "Öğrenci Soyadı",
            "ogrenciCinsiyet": "Öğrenci Cinsiyet",
            "ogrenciKulup": "Öğrenci Kulüp",
        }

        widgets = {
            "ogrenciAd": widgets.TextInput(attrs={"class": "form-control"}),
            "ogrenciSoyad": widgets.TextInput(attrs={"class": "form-control"}),
            "ogrenciCinsiyet": widgets.Select(attrs={"class": "form-control"}),
            "ogrenciKulup": widgets.Select(attrs={"class": "form-control"}),
        }


class NotlarForm(forms.ModelForm):
    class Meta:
        model = models.Notlar
        fields = [
            "dersId",
            "ogrenciId",
            "sinav1",
            "sinav2",
            "sinav3",
            "proje",
        ]

        """dersId = forms.ModelMultipleChoiceField(
            queryset=models.Dersler.objects.all(),
            widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        )"""

        """ogrenciId = forms.ModelChoiceField(
            queryset=models.Ogrenciler.objects.all(),
            empty_label=None,
            widget=forms.SelectDateWidget(attrs={"class": "form-control"}),
        )"""

        labels = {
            "dersId": "Ders Adı",
            "ogrenciId": "Öğrenci Adı",
            "sinav1": "Sınav 1",
            "sinav2": "Sınav 2",
            "sinav3": "Sınav 3",
            "proje": "Proje",
        }

        widgets = {
            "dersId": widgets.SelectMultiple(attrs={"class": "form-control"}),
            "ogrenciId": widgets.SelectMultiple(attrs={"class": "form-control"}),
            "sinav1": widgets.TextInput(attrs={"class": "form-control"}),
            "sinav2": widgets.TextInput(attrs={"class": "form-control"}),
            "sinav3": widgets.TextInput(attrs={"class": "form-control"}),
            "proje": widgets.TextInput(attrs={"class": "form-control"}),
        }


class DersForm(forms.ModelForm):
    class Meta:
        model = models.Dersler
        fields = ['dersAd']
        labels = {
            "dersAd": "Ders Adı"
        }
        widgets = {
            'dersAd': widgets.TextInput(attrs={"class": "form-control"})
        }
