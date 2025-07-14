import pandas as pd
import matplotlib.pyplot as plt
from toolz.curried import pipe, map, filter

# 1. Chargement du fichier
def load_data(filepath):
    return pd.read_csv(filepath)

# 2. Nettoyage (drop lignes nulles)
def clean_data(df):
    return df.dropna()

# 3. Extraction du mois depuis la colonne date
def extract_month(df):
    df = df.copy()
    df["Formatted Date"] = pd.to_datetime(df["Formatted Date"], utc=True)
    df["Mois"] = df["Formatted Date"].dt.month
    return df

# 4. Moyenne des températures par mois
def moyenne_temperature_par_mois(df):
    print("\n🌡️ Moyenne des températures par mois :")
    moyennes = (
        df.groupby("Mois")["Temperature (C)"]
        .mean()
        .round(2)
        .sort_index()
    )
    print(moyennes)
    return moyennes

# 5. Graphique des températures
def plot_temperature_par_mois(moyennes):
    plt.figure(figsize=(10, 6))
    moyennes.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Température moyenne par mois")
    plt.xlabel("Mois")
    plt.ylabel("Température (°C)")
    plt.xticks(rotation=0)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

# 6. Pipeline fonctionnel complet
def process_weather_data(filepath):
    return pipe(
        filepath,
        load_data,
        clean_data,
        extract_month
    )

# 7. Point d’entrée
if __name__ == "__main__":
    df = process_weather_data("C:/Users/mehdi/TP/data/weatherHistory.csv")
    print(df.head())  # aperçu des données transformées

    moyennes = moyenne_temperature_par_mois(df)
    plot_temperature_par_mois(moyennes)
