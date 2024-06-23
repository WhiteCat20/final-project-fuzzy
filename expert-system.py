import pandas as pd


def kategori_tps(tps, lb, pm, rule_base_df):
    # Mencari aturan yang sesuai dalam rule base
    condition = (rule_base_df['TPS'] == tps) & (
        rule_base_df['LB'] == lb) & (rule_base_df['PM'] == pm)
    matches = rule_base_df[condition]

    # Jika ada aturan yang cocok, kembalikan nilai TARGET dari aturan pertama yang cocok
    if not matches.empty:
        return matches.iloc[0]['TARGET']
    else:
        return 'Cek lagi'  # Jika tidak ada aturan yang cocok, kembalikan 'Cek lagi'


def main():
    # Membaca rule_base.xlsx sebagai rule base
    rule_base_path = 'dataset.xlsx'
    df_rule_base = pd.read_excel(
        rule_base_path, sheet_name='Rule Base - Final')

    # List untuk menyimpan hasil kategori_tps
    results = []

    # Contoh nilai random yang akan dimasukkan (Anda dapat mengganti dengan nilai lain)
    input_data = [
        ('Nalar Bagus', 'Sedang', 'Rendah'),
        ('Bagus', 'Tinggi', 'Sedang'),
        ('Nalar Bagus', 'Rendah', 'Tinggi')
        # Tambahkan nilai random lainnya jika diperlukan
    ]

    # Iterasi melalui setiap kombinasi input_data dan cetak hasil kategori_tps
    for tps, lb, pm in input_data:
        output = kategori_tps(tps, lb, pm, df_rule_base)
        results.append((tps, lb, pm, output))
        print(f'TPS: {tps}, LB: {lb}, PM: {pm} -> TARGET: {output}')


if __name__ == "__main__":
    main()
