import tkinter as tk
from tkinter import messagebox

def proses_sugeno():
    try:
        str_ipk = entry_ipk.get().replace(",", ".")
        nilai_ipk = float(str_ipk)
        
        if nilai_ipk < 0.0 or nilai_ipk > 4.0:
            messagebox.showwarning("Peringatan", "Nilai IPK tidak valid! Masukkan angka antara 0.0 sampai 4.0")
            return
            
        poin_prestasi = float(entry_prestasi.get())
        if poin_prestasi < 0 or poin_prestasi > 100:
            messagebox.showwarning("Peringatan", "Nilai Prestasi tidak valid! Masukkan angka antara 0 sampai 100")
            return
            
        str_gaji = entry_penghasilan.get().replace(".", "").replace(",", "")
        gaji = float(str_gaji) / 1000000
        
        jml_tanggungan = float(entry_tanggungan.get())

        if nilai_ipk <= 2.5:
            ipk_rendah = 1
        elif nilai_ipk < 3.0:
            ipk_rendah = (3.0 - nilai_ipk) / 0.5
        else:
            ipk_rendah = 0

        if nilai_ipk <= 2.5 or nilai_ipk >= 3.5:
            ipk_sedang = 0
        elif nilai_ipk <= 3.0:
            ipk_sedang = (nilai_ipk - 2.5) / 0.5
        else:
            ipk_sedang = (3.5 - nilai_ipk) / 0.5

        if nilai_ipk <= 3.0:
            ipk_tinggi = 0
        elif nilai_ipk < 3.5:
            ipk_tinggi = (nilai_ipk - 3.0) / 0.5
        else:
            ipk_tinggi = 1

        if gaji <= 3:
            peng_rendah = 1
        elif gaji < 5:
            peng_rendah = (5 - gaji) / 2
        else:
            peng_rendah = 0

        if gaji <= 3 or gaji >= 7:
            peng_sedang = 0
        elif gaji <= 5:
            peng_sedang = (gaji - 3) / 2
        else:
            peng_sedang = (7 - gaji) / 2

        if gaji <= 5:
            peng_tinggi = 0
        elif gaji < 7:
            peng_tinggi = (gaji - 5) / 2
        else:
            peng_tinggi = 1

        if jml_tanggungan <= 2:
            tang_sedikit = 1
        elif jml_tanggungan < 3:
            tang_sedikit = (3 - jml_tanggungan) / 1
        else:
            tang_sedikit = 0

        if jml_tanggungan <= 2:
            tang_banyak = 0
        elif jml_tanggungan < 3:
            tang_banyak = (jml_tanggungan - 2) / 1
        else:
            tang_banyak = 1
        
        if poin_prestasi <= 40:
            pres_rendah = 1
        elif poin_prestasi < 60:
            pres_rendah = (60 - poin_prestasi) / 20
        else:
            pres_rendah = 0

        if poin_prestasi <= 40:
            pres_tinggi = 0
        elif poin_prestasi < 60:
            pres_tinggi = (poin_prestasi - 40) / 20
        else:
            pres_tinggi = 1

        z_tinggi = 100
        z_sedang = 60
        z_rendah = 30
        
        a1 = min(ipk_tinggi, peng_rendah)
        a2 = ipk_rendah
        a3 = peng_tinggi
        a4 = min(ipk_tinggi, peng_sedang, tang_banyak, pres_tinggi)
        a5 = min(ipk_sedang, peng_rendah, tang_banyak, pres_tinggi)
        a6 = min(ipk_rendah, peng_tinggi, tang_sedikit, pres_rendah)
        a7 = min(ipk_sedang, peng_sedang, tang_sedikit, pres_rendah)
        a8 = min(ipk_tinggi, peng_tinggi, pres_tinggi)
        a9 = min(ipk_sedang, peng_sedang)

        total_atas = (a1*z_tinggi) + (a2*z_rendah) + (a3*z_rendah) + (a4*z_tinggi) + (a5*z_tinggi) + (a6*z_rendah) + (a7*z_sedang) + (a8*z_sedang) + (a9*z_sedang)
        total_bawah = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9

        if total_bawah == 0:
            hasil_z = 0
        else:
            hasil_z = total_atas / total_bawah

        faktor_penyebab = []
        if nilai_ipk < 3.0:
            faktor_penyebab.append("IPK kurang")
        if gaji > 5.0:
            faktor_penyebab.append("penghasilan orang tua terlalu besar")
        if poin_prestasi < 60:
            faktor_penyebab.append("poin prestasi terlalu sedikit")
        if jml_tanggungan <= 2:
            faktor_penyebab.append("tanggungan sedikit")
            
        if hasil_z >= 80:
            prioritas = "TINGGI"
            warna_teks = "green"
            alasan = "Alasan: Sangat direkomendasikan karena memenuhi kriteria prioritas utama."
        elif hasil_z >= 60:
            prioritas = "SEDANG"
            warna_teks = "darkorange"
            if len(faktor_penyebab) > 0:
                alasan = f"Alasan: Masuk daftar cadangan. Terdapat catatan karena {', '.join(faktor_penyebab)}."
            else:
                alasan = "Alasan: Memenuhi kelayakan, namun kombinasi variabel belum mencapai nilai maksimal."
        else:
            prioritas = "RENDAH"
            warna_teks = "red"
            if len(faktor_penyebab) > 0:
                alasan = f"Alasan: Prioritas rendah dikarenakan {', '.join(faktor_penyebab)}."
            else:
                alasan = "Alasan: Kombinasi kriteria secara keseluruhan tidak memenuhi syarat prioritas."
            
        label_hasil.config(text=f"Nilai Prioritas (Z): {hasil_z:.2f}", fg=warna_teks)
        label_kategori.config(text=f"Prioritas Beasiswa: {prioritas}", fg=warna_teks)
        label_alasan.config(text=alasan, fg=warna_teks)

    except ValueError:
        messagebox.showerror("Error", "Mohon isi semua data dengan angka yang benar!")

jendela = tk.Tk()
jendela.title("Sistem Seleksi Beasiswa (Fuzzy Sugeno)")
jendela.geometry("480x500")

tk.Label(jendela, text="IPK (0.0 - 4.0):").pack(pady=(15, 0))
entry_ipk = tk.Entry(jendela, justify='center')
entry_ipk.pack()

tk.Label(jendela, text="Penghasilan (Rp, misal 5.000.000):").pack(pady=(10, 0))
entry_penghasilan = tk.Entry(jendela, justify='center')
entry_penghasilan.pack()

tk.Label(jendela, text="Tanggungan (Orang):").pack(pady=(10, 0))
entry_tanggungan = tk.Entry(jendela, justify='center')
entry_tanggungan.pack()

tk.Label(jendela, text="Prestasi (0 - 100 Poin):").pack(pady=(10, 0))
entry_prestasi = tk.Entry(jendela, justify='center')
entry_prestasi.pack()

tk.Button(jendela, text="Hitung Prioritas", command=proses_sugeno, bg="maroon", fg="white", font=('Helvetica', 11, 'bold')).pack(pady=20)

label_hasil = tk.Label(jendela, text="Nilai Prioritas (Z): -", font=('Helvetica', 16, 'bold'))
label_hasil.pack()

label_kategori = tk.Label(jendela, text="Prioritas Beasiswa: -", font=('Helvetica', 13, 'bold'))
label_kategori.pack(pady=5)

label_alasan = tk.Label(jendela, text="", font=('Helvetica', 10), justify="center", wraplength=400)
label_alasan.pack(pady=(0, 15))

teks_info = (
    "Z adalah output 'Crisp Value' dari perhitungan Fuzzy Sugeno.\n"
    "Nilai Z mewakili skor kelayakan pendaftar (Rentang 30-100).\n"
    "Semakin tinggi Z, semakin besar peluang mendapatkan beasiswa."
)   
tk.Label(jendela, text=teks_info, font=('Helvetica', 9, 'italic'), fg="black", justify="center").pack(pady=10)

jendela.mainloop()