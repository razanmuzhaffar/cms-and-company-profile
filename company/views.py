from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Profil, Produk, Artikel, Galeri
from .forms import KontakForm


def home(request):
    profil = Profil.objects.first()
    layanan_unggulan = Produk.objects.all()[:3]
    artikel_terbaru = Artikel.objects.all()[:3]
    context = {
        'profil': profil,
        'layanan_unggulan': layanan_unggulan,
        'artikel_terbaru': artikel_terbaru,
    }
    return render(request, 'company/home.html', context)


def profil_view(request):
    profil = Profil.objects.first()
    return render(request, 'company/profil.html', {'profil': profil})


def produk_list(request):
    produk = Produk.objects.all()
    return render(request, 'company/produk_list.html', {'produk': produk})


def produk_detail(request, pk):
    item = get_object_or_404(Produk, pk=pk)
    return render(request, 'company/produk_detail.html', {'item': item})


def artikel_list(request):
    artikel = Artikel.objects.all()
    return render(request, 'company/artikel_list.html', {'artikel': artikel})


def artikel_detail(request, pk):
    item = get_object_or_404(Artikel, pk=pk)
    return render(request, 'company/artikel_detail.html', {'item': item})


def galeri_view(request):
    galeri = Galeri.objects.all()
    return render(request, 'company/galeri.html', {'galeri': galeri})


def kontak_view(request):
    profil = Profil.objects.first()

    if request.method == 'POST':
        form = KontakForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pesan Anda berhasil dikirim. Terima kasih!')
            return redirect('company:kontak')
    else:
        form = KontakForm()

    return render(request, 'company/kontak.html', {'profil': profil, 'form': form})