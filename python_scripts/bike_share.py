import pandas as pd
import matplotlib.pyplot as plt

def load_data(filepath):
    """Load dataset and rename columns for clarity."""
    df = pd.read_csv(filepath)
    df.columns = ['Time Stamp', 'Count', 'Temperature', 'F_Temp', 'Humidity',
                  'Wind Speed', 'Weather Code', 'Is Holiday', 'Is Weekend', 'Season']
    return df

def preview_data(df):
    print("Total Rows:", len(df))
    print("\nFirst 24 Rows:\n", df.head(24))
    print("\nLast 24 Rows:\n", df.tail(24))

def max_bike_count(df):
    print("Maximum Bike Share Count:", df['Count'].max())

def seasonal_averages(df):
    season_avg = df.groupby('Season')['Count'].mean()
    print("\nAverage Bike Shares by Season:\n", season_avg)

def hottest_weather(df):
    hottest = df.loc[df['Temperature'].idxmax()]
    print("\nHottest Hour Entry:\n", hottest)

def coldest_weather(df):
    coldest = df.loc[df['Temperature'].idxmin()]
    print("\nColdest Hour Entry:\n", coldest)

def windiest_condition(df):
    windiest = df.loc[df['Wind Speed'].idxmax()]
    print("\nWindiest Hour Entry:\n", windiest)

def seasonal_extremes(df):
    winter_low = df[df['Season'] == 3]['Count'].min()
    autumn_high = df[df['Season'] == 4]['Count'].max()
    spring_humidity = df[df['Season'] == 1]['Humidity'].mean()

    print("\nWinter - Lowest Bike Count:", winter_low)
    print("Autumn - Highest Bike Count:", autumn_high)
    print("Spring - Average Humidity:", spring_humidity)

def scatter_plot(df):
    plt.figure(figsize=(8,6))
    plt.scatter(df['Temperature'], df['Count'], alpha=0.6, edgecolors='w')
    plt.title("Bike Shares vs Temperature")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Share Count")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("visuals/scatter_temperature_vs_count.png")
    plt.close()

def pie_chart(df):
    season_totals = df.groupby('Season')['Count'].sum()
    plt.figure(figsize=(6,6))
    plt.pie(season_totals, labels=season_totals.index, autopct='%1.1f%%', startangle=90)
    plt.title("Bike Shares by Season")
    plt.tight_layout()
    plt.savefig("visuals/pie_chart_season_distribution.png")
    plt.close()

# 🔽 Execute analysis
if __name__ == "__main__":
    df = load_data("data/Bike_Share_London.csv")
    preview_data(df)
    max_bike_count(df)
    seasonal_averages(df)
    hottest_weather(df)
    coldest_weather(df)
    windiest_condition(df)
    seasonal_extremes(df)
    scatter_plot(df)
    pie_chart(df)
