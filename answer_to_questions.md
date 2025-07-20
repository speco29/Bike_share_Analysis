# ✅ Answers to Data Analysis Objectives – Bike Share London Project

This document provides detailed answers to key analysis objectives for the Bike Share London dataset. Each question was explored using Python (`pandas`, `matplotlib`), revealing insights into bike usage patterns based on weather and seasonality.

---

### 🔢 7. Find the Highest Bike Share Count
- **Method:** `DataSet['Count'].max()`
- **Answer:** `1987`
- The highest single recorded bike share count in the dataset.

---

### 🌳 8. Group the Dataset by Season
- **Method:** `DataSet.groupby("Season")`
- The dataset is grouped into four seasons:  
  - `0`: Summer  
  - `1`: Spring  
  - `3`: Winter  
  - `4`: Autumn

---

### 📉 9. Calculate the Average Bike Share Count of All Seasons
- **Method:** `DataSet.groupby("Season")["Count"].mean()`
- **Results:**
  - Summer: `1107.7`
  - Spring: `1071.3`
  - Winter: `979.5`
  - Autumn: `1131.8`
- **Insight:** Autumn has the highest average; winter has the lowest.

---

### 🔥 10. Find the Number of Bike Shares When the Weather Is Hottest
- **Method:** `DataSet[DataSet["Temperature"].max() == DataSet["Temperature"]]`
- **Result:**  
  `1878` bike shares on `13/09/2016 13:00` with `33°C`.

---

### ❄️ 11. Find the Number of Bike Shares When the Weather Is Coldest
- **Method:** `DataSet[DataSet["Temperature"].min() == DataSet["Temperature"]]`
- **Result:**  
  `204` bike shares on `19/01/2015 05:00` with `-5°C`.

---

### 🌬️ 12. Find the Number of Bike Shares When the Wind Speed Is Highest
- **Method:** `DataSet[DataSet["Wind Speed"].max() == DataSet["Wind Speed"]]`
- **Result:**  
  Wind speed of `56 km/h` and `1401` bike shares.

---

### 🧊 13. Find the Lowest Number of Bike Shares in Winter
- **Method:**  
  ```python
  Winter = DataSet.groupby("Season").get_group(3)  
  Winter["Count"].min()
  ```
- **Result:**
  7 bike shares — the lowest winter value.

---

### 🍂 14. Find the Highest Number of Bike Shares in Autumn
- **Method:**
  ```python
  Autumn = DataSet.groupby("Season").get_group(4)  
  Autumn["Count"].max()
  ```
- **Result:**
  1987 bike shares — highest in autumn and overall.

---

### 🌸 15. Find the Average Humidity in Spring
- **Method:**
  ```python
  Spring = DataSet.groupby("Season").get_group(1)  
  Spring["Humidity"].mean()
  ```
- **Result:**
  60.1% (approximate)

---

### 📈 16. Scatter Chart – Number of Bike Shares by Temperature
- **Method:** `plt.scatter(DataSet["Temperature"], DataSet["Count"], alpha=0.6)`
- **Result:**
  Shows positive correlation between temperature and bike share usage.
  📁 Saved As: visuals/scatter_temperature_vs_count.png

---

### 🥧 17. Pie Chart – Distribution of Bike Shares by Season
- **Method:**
  ```python
    season_totals = DataSet.groupby("Season")["Count"].sum()  
    plt.pie(season_totals)
  ```
 - **Result:**
  Autumn and summer contribute the most to total shares.
  📁 Saved As: visuals/pie_chart_season_distribution.png

