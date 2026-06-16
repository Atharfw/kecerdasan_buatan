import tkinter as tk
from tkinter import messagebox

def hitung_sugeno():
    try:
        ipk = float(entry_ipk.get())
        penghasilan = float(entry_penghasilan.get())
        tanggungan = float(entry_tanggungan.get())
        prestasi = float(entry_prestasi.get())

        ipk_rendah = 1 if ipk <= 2.5 else (3.0 - ipk)/0.5 if ipk < 3.0 else 0
        ipk_sedang = 0 if ipk <= 2.5 or ipk >= 3.5 else (ipk - 2.5)/0.5 if ipk <= 3.0 else (3.5 - ipk)/0.5
        ipk_tinggi = 0 if ipk <= 3.0 else (ipk - 3.0)/0.5 if ipk < 3.5 else 1

        peng_rendah = 1 if penghasilan <= 3 else (5 - penghasilan)/2 if penghasilan < 5 else 0
        peng_sedang = 0 if penghasilan <= 3 or penghasilan >= 7 else (penghasilan - 3)/2 if penghasilan <= 5 else (7 - penghasilan)/2
        peng_tinggi = 0 if penghasilan <= 5 else (penghasilan - 5)/2 if penghasilan < 7 else 1

        tang_sedikit = 1 if tanggungan <= 2 else (3 - tanggungan)/1 if tanggungan < 3 else 0
        tang_banyak = 0 if tanggungan <= 2 else (tanggungan - 2)/1 if tanggungan < 3 else 1
        pres_rendah = 1 if prestasi <= 40 else (60 - prestasi)/20 if prestasi < 60 else 0
        pres_tinggi = 0 if prestasi <= 40 else (prestasi - 40)/20 if prestasi < 60 else 1

        z1, z2, z3, z4, z5, z6, z7, z8, z9 = 100, 60, 100, 30, 30, 30, 60, 60, 100
        
        a1 = min(ipk_tinggi, peng_rendah, tang_banyak, pres_tinggi)
        a2 = min(ipk_tinggi, peng_sedang, tang_sedikit, pres_rendah)
        a3 = min(ipk_sedang, peng_rendah, tang_banyak, pres_tinggi)
        a4 = min(ipk_sedang, peng_sedang, tang_sedikit, pres_rendah)
        a5 = ipk_rendah
        a6 = peng_tinggi
        a7 = min(ipk_sedang, peng_rendah, pres_rendah)
        a8 = min(ipk_tinggi, peng_tinggi, pres_tinggi)
        a9 = min(ipk_tinggi, tang_banyak, pres_rendah)

        atas = (a1*z1) + (a2*z2) + (a3*z3) + (a4*z4) + (a5*z5) + (a6*z6) + (a7*z7) + (a8*z8) + (a9*z9)
        bawah = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9

        if bawah == 0:
            hasil_z = 0
        else:
            hasil_z = atas / bawah
            
        label_hasil.config(text=f"Nilai Prioritas (Z): {hasil_z:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Mohon masukkan angka yang valid!")

root = tk.Tk()
root.title("Sistem Seleksi Beasiswa (Fuzzy Sugeno)")
root.geometry("350x300")

tk.Label(root, text="IPK (0.0 - 4.0):").pack()
entry_ipk = tk.Entry(root)
entry_ipk.pack()

tk.Label(root, text="Penghasilan (Juta, misal 4):").pack()
entry_penghasilan = tk.Entry(root)
entry_penghasilan.pack()

tk.Label(root, text="Tanggungan (Orang):").pack()
entry_tanggungan = tk.Entry(root)
entry_tanggungan.pack()

tk.Label(root, text="Prestasi (0 - 100 Poin):").pack()
entry_prestasi = tk.Entry(root)
entry_prestasi.pack()
tk.Button(root, text="Hitung Prioritas", command=hitung_sugeno).pack(pady=10)
label_hasil = tk.Label(root, text="Nilai Prioritas (Z): -", font=('Helvetica', 12, 'bold'))

label_hasil.pack()
root.mainloop()