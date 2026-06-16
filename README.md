#Sistem Seleksi Penerima Beasiswa (Logika Fuzzy Sugeno)

Halo Ibu **Anis Fitri Nur Masruriyah, S.Kom., M.Kom.** selaku dosen pengampu mata kuliah Kecerdasan Buatan. Izinkan kami dari **Kelompok 3** untuk memperkenalkan diri:

| Peran | Nama Lengkap | NIM |
| :--- | :--- | :--- |
| **Ketua** | Athar Fajle Mawla Wicaksono | 2410511155 |
| **Anggota** | M. Nazhmi Rabbani Firdaus | 2410511157 |
| **Anggota** | M. Habibie Wibisono | 2410511138 |
| **Anggota** | Piere Valkyrie | 2410511152 |

---
**Program Studi S1 Informatika | UPN "Veteran" Jakarta**
---

##Deskripsi Proyek
Repositori ini berisi implementasi **Logika Fuzzy dengan Metode Sugeno (Orde-Nol)** untuk memecahkan studi kasus penentuan prioritas penerimaan beasiswa mahasiswa. Program ini dibangun menggunakan bahasa pemrograman Python dengan antarmuka grafis (GUI) interaktif menggunakan library `Tkinter`.

Sistem ini memproses 4 variabel *input* utama:
1. **IPK** (Skala 0.0 - 4.0)
2. **Penghasilan Orang Tua** (Dalam format Rupiah)
3. **Jumlah Tanggungan** (Orang)
4. **Prestasi Non-Akademik** (Skala Poin 0 - 100)

Melalui proses *Fuzzifikasi*, *Inferensi* (berdasarkan 9 aturan/rules yang telah didesain), dan *Defuzzifikasi* (Weighted Average), sistem akan mengeluarkan *output* berupa nilai *Crisp* (Z) yang merepresentasikan **Tingkat Prioritas Beasiswa**.

##Cara Menjalankan Aplikasi
1. Pastikan Python sudah terinstal di PC/Laptop Anda.
2. Clone repositori ini:
   ```bash
   git clone [https://github.com/](https://github.com/)[Atharfw]/[kecerdasan_buatan].git
