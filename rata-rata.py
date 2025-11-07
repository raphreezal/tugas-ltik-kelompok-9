import pandas as pd

def hitung_rata_rata(file_csv):
    # Baca file CSV
    df = pd.read_csv(file_csv)
    
    # Pilih hanya kolom numerik
    numeric_cols = df.select_dtypes(include='number')
    
    # Hitung rata-rata tiap kolom
    rata_rata = numeric_cols.mean()
    
    print("Rata-rata tiap kolom:")
    print(rata_rata)

hitung_rata_rata('data.csv')
