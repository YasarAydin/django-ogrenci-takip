from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect, get_object_or_404
from . import models
from . import forms


# Create your views here.

def index(request):
    return render(request, "index.html")


def ogrenciler(request):
    ogrencilerVerisi = models.Ogrenciler.objects.all()
    return render(request, "ogrenciler/index.html", context={
        "ogrencilerVerisi": ogrencilerVerisi
    })


def ogrenci_ekle(request):
    if request.method == "POST":
        ogrenciForm = forms.OgrenciForm(request.POST)
        if ogrenciForm.is_valid():
            ogrenciForm.save()
            return redirect('ogrenciler')
    else:
        ogrenciForm = forms.OgrenciForm()
    return render(request, "ogrenciler/yeni_ogrenci_ekle.html", context={
        "ogrenciForm": ogrenciForm
    })


def ogrenci_guncelle(request, id):
    ogrenci = get_object_or_404(models.Ogrenciler, pk=id)
    if request.method == "POST":
        ogrenciForm = forms.OgrenciForm(request.POST, instance=ogrenci)
        if ogrenciForm.is_valid():
            ogrenciForm.save()
            return redirect('ogrenciler')
    else:
        ogrenciForm = forms.OgrenciForm(instance=ogrenci)
    return render(request, "ogrenciler/ogrenci_guncelle.html", context={
        "ogrenciForm": ogrenciForm
    })


def ogrenci_sil(request, id):
    ogrencilerVerisi = models.Ogrenciler.objects.get(id=id)
    if ogrencilerVerisi.delete():
        return redirect("ogrenciler")
    return render(request, "ogrenciler/index.html")


def notlar(request):
    notlarListesi = models.Notlar.objects.all()
    for a in notlarListesi:
        # a.remove()
        a.save()

    return render(request, "notlar/index.html", context={
        "notlarListesi": notlarListesi,
    })


def not_ekle(request):
    if request.method == "POST":
        notForm = forms.NotlarForm(request.POST)
        if notForm.is_valid():
            notForm.save()
            return redirect('notlar')
    else:
        notForm = forms.NotlarForm()
    return render(request, "notlar/yeni_not_ekle.html", context={
        "notForm": notForm
    })


def not_guncelle(request, id):
    notum = get_object_or_404(models.Notlar, pk=id)
    if request.method == "POST":
        notForm = forms.NotlarForm(request.POST, instance=notum)
        if notForm.is_valid():
            notForm.save()
            return redirect('notlar')
    else:
        notForm = forms.NotlarForm(instance=notum)
    return render(request, "notlar/not_guncelle.html", context={
        "notForm": notForm
    })


def not_sil(request, id):
    notum = models.Notlar.objects.get(id=id)
    if notum.delete():
        return redirect('notlar')
    return render(request, "dersler/index.html")


def kulupler(request):
    kuluplerListesi = models.Kulupler.objects.all()
    return render(request, "kulupler/index.html", context={
        "kuluplerListesi": kuluplerListesi,
    })


def kulup_ekle(request):
    if request.method == "POST":
        form = forms.KulupForm(request.POST)
        if form.is_valid():
            sKulupAd = form.cleaned_data["kulupAd"]
            sKulupKontenjan = form.cleaned_data["kulupKontenjan"]
            sKulup = models.Kulupler(kulupAd=sKulupAd, kulupKontenjan=sKulupKontenjan)
            sKulup.save()
            return redirect('kulupler')
    else:
        form = forms.KulupForm()
    return render(request, "kulupler/yeni_kulup_ekle.html", context={
        "form": form
    })


def kulup_guncelle(request, id):
    kulup = get_object_or_404(models.Kulupler, pk=id)
    if request.method == "POST":
        kulupForm = forms.KulupForm(request.POST, instance=kulup)
        if kulupForm.is_valid():
            kulupForm.save()
            return redirect('kulupler')
    else:
        kulupForm = forms.KulupForm(instance=kulup)
    return render(request, "kulupler/kulup_guncelle.html", context={
        "kulupForm": kulupForm
    })


def kulup_sil(request, id):
    kulupVerisi = models.Kulupler.objects.get(id=id)
    if kulupVerisi.delete():
        return redirect('kulupler')
    return render(request, "kulupler/index.html")


def dersler(request):
    derslerListesi = models.Dersler.objects.all()
    return render(request, "dersler/index.html", context={
        "derslerListesi": derslerListesi,
    })


def ders_ekle(request):
    if request.method == "POST":
        form = forms.DersForm(request.POST)
        if form.is_valid():
            sDersAd = form.cleaned_data["dersAd"]
            sDers = models.Dersler(dersAd=sDersAd)
            sDers.save()
            return redirect('dersler')
    else:
        form = forms.DersForm()
    return render(request, "dersler/yeni_ders_ekle.html", context={
        "form": form
    })


def ders_guncelle(request, id):
    ders = get_object_or_404(models.Dersler, pk=id)
    if request.method == "POST":
        dersForm = forms.DersForm(request.POST, instance=ders)
        if dersForm.is_valid():
            dersForm.save()
            return redirect('dersler')
    else:
        dersForm = forms.DersForm(instance=ders)
    return render(request, "dersler/ders_guncelle.html", context={
        "dersForm": dersForm
    })


def ders_sil(request, id):
    dersVerisi = models.Dersler.objects.get(id=id)
    if dersVerisi.delete():
        return redirect('dersler')
    return render(request, "dersler/index.html")
