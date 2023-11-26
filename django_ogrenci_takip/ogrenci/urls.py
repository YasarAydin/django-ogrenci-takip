from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ogrenciler, name="index"),

    path('ogrenciler', views.ogrenciler, name="ogrenciler"),
    path('ogrenciler/ekle/', views.ogrenci_ekle, name="ogrenci_ekle"),
    path('ogrenciler/guncelle/<int:id>', views.ogrenci_guncelle, name="ogrenci_guncelle"),
    path('ogrenciler/sil/<int:id>', views.ogrenci_sil, name="ogrenci_sil"),

    path('notlar', views.notlar, name="notlar"),
    path('notlar/ekle/', views.not_ekle, name="not_ekle"),
    path('notlar/guncelle/<int:id>', views.not_guncelle, name="not_guncelle"),
    path('notlar/sil/<int:id>', views.not_sil, name="not_sil"),

    path('kulupler', views.kulupler, name="kulupler"),
    path('kulupler/ekle/', views.kulup_ekle, name="kulup_ekle"),
    path('kulupler/guncelle/<int:id>', views.kulup_guncelle, name="kulup_guncelle"),
    path('kulupler/sil/<int:id>', views.kulup_sil, name="kulup_sil"),

    path('dersler', views.dersler, name="dersler"),
    path('dersler/ekle', views.ders_ekle, name="ders_ekle"),
    path('dersler/guncelle/<int:id>', views.ders_guncelle, name="ders_guncelle"),
    path('dersler/sil/<int:id>', views.ders_sil, name="ders_sil"),
]
