import pandas as pd


def kategori_lb(lng, lnd, rule_base_df):

    # Mencari aturan yang sesuai dalam rule base (dataset.xlsx)
    condition = (rule_base_df['LNG'] == lng) & (rule_base_df['LND'] == lnd)
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

    df_input = df_fuzzifikasi[['LNG', 'LND']]

    # Membaca dataset.xlsx sebagai rule base
    rule_base_path = 'dataset.xlsx'
    rule_base_sheet = 'Rule Base - LB'
    df_rule_base = pd.read_excel(rule_base_path, sheet_name=rule_base_sheet)

    # List untuk menyimpan hasil kategori_lb
    results = []

    # Iterasi melalui setiap baris df_input dan cetak hasil kategori_lb
    for index, row in df_input.iterrows():
        lng = row['LNG']
        lnd = row['LND']

        output = kategori_lb(lng, lnd, df_rule_base)
        print(f'{index+2} - {output}')
        results.append(output)

    # Menambahkan hasil ke dalam DataFrame df_fuzzifikasi
    df_fuzzifikasi['OUTPUT'] = results

    # Menyimpan hasil ke dalam file excel baru
    output_path = 'output/hasil_kategorisasi_lb.xlsx'
    df_fuzzifikasi.to_excel(output_path, index=False)

    print(f"Hasil kategorisasi disimpan di {output_path}")


if __name__ == "__main__":
    main()
