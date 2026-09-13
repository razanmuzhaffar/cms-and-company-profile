from django.db import models


class Profil(models.Model):
    """Data profil perusahaan (Sejarah, Visi, Misi, Nilai) — diedit lewat admin."""
    nama_perusahaan = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='profil/', blank=True, null=True)
    sejarah = models.TextField()
    visi = models.TextField()
    misi = models.TextField()
    nilai_perusahaan = models.TextField()
    alamat = models.CharField(max_length=255)
    telepon = models.CharField(max_length=20)
    email = models.EmailField()
    google_maps_embed = models.TextField(blank=True)

    class Meta:
        db_table = 'profil'
        verbose_name = 'Profil Perusahaan'
        verbose_name_plural = 'Profil Perusahaan'

    def __str__(self):
        return self.nama_perusahaan


class Produk(models.Model):
    nama_layanan = models.CharField(max_length=200)
    gambar = models.ImageField(upload_to='produk/')
    deskripsi_singkat = models.CharField(max_length=255)
    deskripsi_lengkap = models.TextField()
    dibuat_pada = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'produk'
        verbose_name = 'Produk'
        verbose_name_plural = 'Produk'

    def __str__(self):
        return self.nama_layanan


class Artikel(models.Model):
    judul = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='artikel/')
    ringkasan = models.CharField(max_length=255)
    isi = models.TextField()
    tanggal_terbit = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'artikel'
        verbose_name = 'Artikel'
        verbose_name_plural = 'Artikel'

    def __str__(self):
        return self.judul


class Galeri(models.Model):
    judul = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='galeri/')
    diunggah_pada = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'galeri'
        verbose_name = 'Galeri'
        verbose_name_plural = 'Galeri'

    def __str__(self):
        return self.judul


class PesanKontak(models.Model):
    nama = models.CharField(max_length=150)
    email = models.EmailField()
    subjek = models.CharField(max_length=200)
    pesan = models.TextField()
    dikirim_pada = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'pesankontak'
        verbose_name = 'Pesan Kontak'
        verbose_name_plural = 'Pesan Kontak'

    def __str__(self):
        return f"{self.nama} - {self.subjek}"
