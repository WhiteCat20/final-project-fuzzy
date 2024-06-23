import pandas as pd
import numpy as np
import skfuzzy as fuzz
import csv

# Baca dataset
excel = pd.read_excel('dataset.xlsx', sheet_name='Dataset-2')
df = pd.DataFrame(excel)

# Definisi rentang nilai dan fungsi keanggotaan untuk setiap variabel
variables = {
    'KPU': {'low': 319, 'mid': 500, 'high': 800},
    'PPU': {'low': 319, 'mid': 500, 'high': 800},
    'PPM': {'low': 319, 'mid': 500, 'high': 800},
    'PM2': {'low': 319, 'mid': 500, 'high': 800},
    'LNG': {'low': 319, 'mid': 500, 'high': 800},
    'LND': {'low': 319, 'mid': 500, 'high': 800},
    'PM': {'low': 319, 'mid': 500, 'high': 800}
}

# Fungsi untuk fuzzifikasi nilai
def fuzzifikasi_nilai(nilai, var):
    low = variables[var]['low']
    mid = variables[var]['mid']
    high = variables[var]['high']
    x = np.arange(low, high, 1)
    rendah = fuzz.trimf(x, [low, low, mid])
    normal = fuzz.trimf(x, [low, mid, high])
    tinggi = fuzz.trimf(x, [mid, high, high])
    derajat_rendah = fuzz.interp_membership(x, rendah, nilai)
    derajat_normal = fuzz.interp_membership(x, normal, nilai)
    derajat_tinggi = fuzz.interp_membership(x, tinggi, nilai)
    return derajat_rendah, derajat_normal, derajat_tinggi

# Simpan hasil fuzzifikasi ke dalam satu file CSV
output_csv = 'output/hasil_fuzzifikasi.csv'
with open(output_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Tulis header
    writer.writerow(['KPU', 'PPU', 'PPM', 'PM2', 'LNG', 'LND', 'PM'])
    
    # Melakukan fuzzifikasi untuk setiap variabel
    for idx, row in df.iterrows():
        hasil_fuzzifikasi = []
        for var in variables:
            nilai = row[var]
            hasil_rendah, hasil_normal, hasil_tinggi = fuzzifikasi_nilai(nilai, var)
            nilai_defuzzifikasi = np.argmax([hasil_rendah, hasil_normal, hasil_tinggi])
            hasil_fuzzifikasi.append(nilai_defuzzifikasi)
        writer.writerow(hasil_fuzzifikasi)

print(f"Hasil fuzzifikasi telah disimpan dalam file {output_csv}")

# Konversi CSV ke Excel
output_excel = 'output/hasil_fuzzifikasi.xlsx'
df_csv = pd.read_csv(output_csv, header=None)
df_csv.to_excel(output_excel, index=False, header=None)

print(f"File CSV {output_csv} berhasil dikonversi ke Excel {output_excel}")
