import pandas as pd


def kategori_tps(kpu, ppu, ppm, pm2, rule_base_df):
    # Mengecek kondisi jika ada 3 atau lebih nilai 0
    if [kpu, ppu, ppm, pm2].count(0) >= 3:
        return 'Tidak Layak'

    # Mengecek kondisi jika ada lebih dari 2 nilai 2
    if [kpu, ppu, ppm, pm2].count(2) > 2:
        return 'Sangat Bagus'

    # Mencari aturan yang sesuai dalam rule base (dataset.xlsx)
    condition = (rule_base_df['KPU'] == kpu) & (rule_base_df['PPU'] == ppu) & (
        rule_base_df['PPM'] == ppm) & (rule_base_df['PM2'] == pm2)
    matches = rule_base_df[condition]

    # Jika ada aturan yang cocok, kembalikan nilai OUTPUT dari aturan pertama yang cocok
    if not matches.empty:
        return matches.iloc[0]['OUTPUT']
    else:
        return 'Cek lagi'  # Jika tidak ada aturan yang cocok, kembalikan 'Cek lagi'


def main():
    # Membaca hasil_fuzzifikasi.xlsx
    fuzzifikasi_path = 'output/hasil_fuzzifikasi.xlsx'
    df_fuzzifikasi = pd.read_excel(fuzzifikasi_path)

    # Hanya mengambil kolom KPU, PPU, PPM, dan PM2 dari hasil fuzzifikasi
    df_input = df_fuzzifikasi[['KPU', 'PPU', 'PPM', 'PM2']]

    # Membaca dataset.xlsx sebagai rule base
    rule_base_path = 'dataset.xlsx'
    rule_base_sheet = 'Rule Base - TPS'
    df_rule_base = pd.read_excel(rule_base_path, sheet_name=rule_base_sheet)

    # List untuk menyimpan hasil kategori_tps
    results = []

    # Iterasi melalui setiap baris df_input dan cetak hasil kategori_tps
    for index, row in df_input.iterrows():
        kpu = row['KPU']
        ppu = row['PPU']
        ppm = row['PPM']
        pm2 = row['PM2']
        output = kategori_tps(kpu, ppu, ppm, pm2, df_rule_base)
        print(f'{index+2} - {output}')
        results.append(output)

    # Menambahkan hasil ke dalam DataFrame df_fuzzifikasi
    df_fuzzifikasi['OUTPUT'] = results

    # Menyimpan hasil ke dalam file excel baru
    output_path = 'output/hasil_kategorisasi_tps.xlsx'
    df_fuzzifikasi.to_excel(output_path, index=False)

    print(f"Hasil kategorisasi disimpan di {output_path}")


if __name__ == "__main__":
    main()
