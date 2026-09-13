from django.contrib import admin
from django.shortcuts import redirect
from .models import Profil, Produk, Artikel, Galeri, PesanKontak

# Branding Django Admin
admin.site.site_header = "Panel Admin Company Profile"
admin.site.site_title = "Admin Company Profile"
admin.site.index_title = "Dashboard Administrasi"


# Profil Perusahaan

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display  = ['nama_perusahaan', 'telepon', 'email']
    search_fields = ['nama_perusahaan', 'sejarah', 'visi', 'misi']
    fieldsets = [
        ('Informasi Umum', {
            'fields': ['nama_perusahaan', 'logo', 'alamat', 'telepon', 'email']
        }),
        ('Tentang Perusahaan', {
            'fields': ['sejarah', 'visi', 'misi', 'nilai_perusahaan']
        }),
        ('Informasi Tambahan', {
            'fields': ['google_maps_embed'],
            'classes': ['collapse'],
        }),
    ]

    def has_add_permission(self, request):
        # Sesuai spesifikasi: Profil Perusahaan HANYA Edit Profil (tidak boleh tambah profil baru)
        return False

    def has_delete_permission(self, request, obj=None):
        # Profil tidak boleh dihapus
        return False

    def changelist_view(self, request, extra_context=None):
        # Saat klik menu 'Profil Perusahaan', langsung buka form Edit Profil
        profil = Profil.objects.first()
        if profil:
            return redirect('admin:company_profil_change', profil.pk)
        return super().changelist_view(request, extra_context=extra_context)


# Produk

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display  = ['nama_layanan', 'deskripsi_singkat', 'dibuat_pada']
    search_fields = ['nama_layanan', 'deskripsi_singkat', 'deskripsi_lengkap']
    list_filter   = ['dibuat_pada']
    ordering      = ['-dibuat_pada']


# Artikel

@admin.register(Artikel)
class ArtikelAdmin(admin.ModelAdmin):
    list_display  = ['judul', 'tanggal_terbit']
    search_fields = ['judul', 'ringkasan', 'isi']
    list_filter   = ['tanggal_terbit']
    ordering      = ['-tanggal_terbit']
    fieldsets = [
        ('Informasi Artikel', {
            'fields': ['judul', 'thumbnail']
        }),
        ('Konten', {
            'fields': ['ringkasan', 'isi']
        }),
    ]


# Galeri

@admin.register(Galeri)
class GaleriAdmin(admin.ModelAdmin):
    list_display  = ['judul', 'foto', 'diunggah_pada']
    list_filter   = ['diunggah_pada']
    search_fields = ['judul']
    ordering      = ['-diunggah_pada']


from django.utils.html import format_html

# Pesan Kontak

@admin.register(PesanKontak)
class PesanKontakAdmin(admin.ModelAdmin):
    list_display    = ['nama', 'email', 'subjek', 'dikirim_pada', 'kirim_email_balasan']
    list_filter     = ['dikirim_pada']      
    search_fields   = ['nama', 'email', 'subjek', 'pesan']
    readonly_fields = ['nama', 'email', 'subjek', 'pesan', 'dikirim_pada', 'kirim_email_balasan']
    ordering        = ['-dikirim_pada']
    fieldsets = [
        ('Informasi Pengirim', {
            'fields': ['nama', 'email', 'kirim_email_balasan']
        }),
        ('Pesan', {
            'fields': ['subjek', 'pesan']
        }),
        ('Informasi Waktu', {
            'fields': ['dikirim_pada'],
            'classes': ['collapse'],
        }),
    ]

    def kirim_email_balasan(self, obj):
        if obj.email:
            return format_html(
                '<a href="mailto:{}?subject=Re: {}">Balas Email</a>',
                obj.email,
                obj.subjek
            )
        return "-"
    kirim_email_balasan.short_description = "Aksi Email"
