from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('', views.home, name='home'),
    path('profil/', views.profil_view, name='profil'),
    path('produk/', views.produk_list, name='produk_list'),
    path('produk/<int:pk>/', views.produk_detail, name='produk_detail'),
    path('artikel/', views.artikel_list, name='artikel_list'),
    path('artikel/<int:pk>/', views.artikel_detail, name='artikel_detail'),
    path('galeri/', views.galeri_view, name='galeri'),
    path('kontak/', views.kontak_view, name='kontak'),
]
