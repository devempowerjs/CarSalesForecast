# Car Sales Trend Analysis & Forecasting

Analyze and visualize trends in a large synthetic car sales dataset. This project provides a modular framework for data analysis, insight extraction, and visualization, enabling you to explore car sales patterns, compare brands, and predict future sales.

## Visualization

<table><tr><td>
      <h3 align="center">Global Top Brand</h3>
      <i>Bar chart showing which brand was the top seller in the most countries for each year.</i><br><br>
      <img width="auto" src="output\global_top_brand.png">
    </td><td>
      <h3 align="center">Sales Comparison</h3>
      <i>Bar chart comparing sales of selected brands across years in chosen countries.</i><br><br>
      <img width="auto" src="output\sales_comparison.png">  </td>
  </tr>
    <tr><td>
      <h3 align="center">Top Selling Brand</h3>
      <i>Line plot showing the top-selling brand in a specific country over time.</i><br><br>
      <img width="auto" src="output\top_selling_brand_usa.png">
    </td><td>
      <h3 align="center">Heatmap of Top Brands</h3>
      <i>Heatmap visualizing the top brand for each country and year.</i><br><br>
      <img width="auto" src="output\top_brand_heatmap.png">
    </td></tr>
</table>
  <h3 align="center">Future Sales Prediction</h3>
  <i>Bar chart showing historical sales and predicted sales for a brand/country/year using linear regression.</i><br><br>
  <img width="auto" src="output\usa_toyota_2025_prediction.png">

## Features

- **Data Preparation:** Standardizes and aggregates raw sales data for analysis
- **Insight Extraction:** Find top brands by country/year, global leaders, and sales totals
- **Visualization:** Generate heatmaps, bar charts, line plots, and prediction plots
- **Sales Prediction:** Predict future sales for a brand in a country using linear regression
- **Customizable:** Easily change countries, brands, and years for your analysis

## Project Structure

```bash
.
├── dataset.py               # Script to download the dataset from KaggleHub
├── dataset/                 # Folder for all CSV files
├── data_utils.py            # Data loading, cleaning functions, standardizing columns, aggregating sales
├── insights.py              # Functions to extract insights
├── plotting.py              # All plotting functions
├── main.py                  # Main script       
├── output/                  # Folder for all generated plots
```

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/devempowerjs/CarSalesForecast.git
cd CarSalesForecast
```

### 2. Install Requirements

```bash
pip install pandas matplotlib seaborn kagglehub scikit-learn
```

### 3. Download the Dataset

```bash
python dataset.py
```

This will download the dataset from KaggleHub and print the file path. Then the CSV file should be manualy placed in the `dataset/` folder.

## How to Use

### 1. Configure Your Analysis

Open `main.py` and edit the parameters at the top to select the country, brand, and years you want to analyze:

```python
COUNTRY = "USA"
BRAND = "Toyota"
COMPARISON_COUNTRIES = ['USA']
COMPARISON_BRANDS = ['Toyota', 'Volkswagen', 'Ford', 'Chrysler', 'Lexus', 'Chevrolet']
COMPARISON_YEARS = [2020, 2021, 2022, 2023, 2024]
PREDICT_YEAR = 2025
TOTAL_SALES_YEAR = 2024
```

### 2. Select Insights/Plots to Run

In `main.py`, comment or uncomment the function calls to run only the analyses or plots you need. Each block is independent and can be enabled/disabled as needed.

### 3. Run the Main Script

```bash
python main.py
```

This will generate the selected plots (saved in `output/`) and print insights to the console.

## Example Analyses

- Compare sales for selected countries, brands, and years
- Show total sales for a specific brand/country/year
- Visualize the global top brand by number of countries each year
- Heatmap of top brands by country and year
- Trend of top-selling brands in a specific country
- Predict future sales for a brand in a country for a specific year (using linear regression)

## Customization

- To analyze different countries, brands, or years, change the lists in `main.py`
- To generate different plots, comment or uncomment the relevant function calls in `main.py`
- All plots will be saved in the `output/` directory for easy access

> [!Note]
>Code is modular; data loading, insights, and plotting are separated for clarity and maintainability. <br>
>Dataset is synthetic and intended for demonstration and educational purposes. <br>

## Source and Attribution

[Synthetic Car Sales Dataset over Million records](https://www.kaggle.com/datasets/jayavarman/synthetic-car-sales-dataset-over-million-records) dataset from Kaggle.
