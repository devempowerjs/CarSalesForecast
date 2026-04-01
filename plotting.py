import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd

sns.set(style="whitegrid")
os.makedirs("output", exist_ok=True)
TOP_BRAND_COLORS = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
    "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"
]

def plot_heatmap(top_per_country_year):
    pivot_table = top_per_country_year.pivot(index='country', columns='year', values='top_brand')
    heatmap_data = pivot_table.apply(lambda x: pd.factorize(x)[0])
    plt.figure(figsize=(16, 8)) 
    sns.heatmap(heatmap_data, cmap="tab20", cbar=False, linewidths=0.1)
    plt.title("Top-Selling Brands by Country")
    plt.xlabel("Year")
    plt.ylabel("Country")
    plt.tight_layout(rect=[0, 0, 0.85, 1])
    plt.savefig("output/top_brand_heatmap.png", bbox_inches='tight')
    plt.show()
    plt.close()

def plot_global_top(global_top):
    plt.figure(figsize=(16, 8))
    unique_brands = global_top['top_brand'].unique()
    palette = {brand: TOP_BRAND_COLORS[i % len(TOP_BRAND_COLORS)] for i, brand in enumerate(unique_brands)}
    ax = sns.barplot(
        data=global_top, x='year', y='countries_count', hue='top_brand', dodge=False, palette=palette
    )
    plt.title("Top Brand by Number of Countries")
    plt.ylabel("Countries Where Brand is #1")
    plt.xticks(rotation=45)
    for p in ax.patches:
        height = p.get_height()
        if height > 0:
            ax.annotate(f"{int(height)}", (p.get_x() + p.get_width() / 2, height),
                        ha='center', va='bottom', fontsize=10)
    plt.legend(title="Top Brand", bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout(rect=[0, 0, 0.85, 1])
    plt.savefig('output/global_top_brand.png', bbox_inches='tight')
    plt.show()
    plt.close()

def plot_country_trend(top_per_country_year, country):
    country_data = top_per_country_year[top_per_country_year['country'] == country]
    plt.figure(figsize=(16, 8))
    ax = sns.lineplot(
        data=country_data, x='year', y='top_sales', hue='top_brand', marker='o', palette='tab10'
    )
    plt.title(f"Top-Selling Brand in {country}")
    plt.ylabel("Units Sold")
    plt.xticks(rotation=45)
    
    for line in ax.lines:
        for x, y in zip(line.get_xdata(), line.get_ydata()):
            if not pd.isna(y):
                ax.annotate(f"{int(y)}", (x, y), textcoords="offset points", xytext=(0, 9),
                            ha='center', fontsize=10, color=line.get_color())
    plt.legend(title="Top Brand", bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout(rect=[0, 0, 0.85, 1])
    plt.savefig(f"output/top_selling_brand_{country.lower()}.png", bbox_inches='tight')
    plt.show()
    plt.close()

def plot_comparison(plot_data, countries, brands, years):
    plot_df = pd.DataFrame(plot_data)
    plt.figure(figsize=(16, 8))
    ax = sns.barplot(
        data=plot_df, x='Year', y='Sales', hue='Brand', ci=None, palette='tab10', dodge=True
    )
    plt.title(f"Sales Comparison: {', '.join(countries)} | Brands: {', '.join(brands)}")
    plt.ylabel("Units Sold")
    plt.xlabel("Year")
    
    for p in ax.patches:
        height = p.get_height()
        if height > 0:
            ax.annotate(f"{int(height)}", (p.get_x() + p.get_width() / 2, height),
                        ha='center', va='bottom', fontsize=10)
    plt.legend(title="Brand", bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout(rect=[0, 0, 0.85, 1])
    plt.savefig("output/sales_comparison.png", bbox_inches='tight')
    plt.show()
    plt.close()

def plot_prediction(df, country, brand, year, predicted_sales):
    history = df[(df['country'] == country) & (df['brand'] == brand)].sort_values('year')
    plt.figure(figsize=(16, 8))
    bars1 = plt.bar(history['year'], history['sales'], color='skyblue', label='Historical Sales')
    bar2 = plt.bar(year, predicted_sales, color='orange', label='Predicted Sales')
    plt.title(f"{brand} Sales in {country}")
    plt.xlabel("Year")
    plt.ylabel("Units Sold")
    
    for bar in bars1:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{int(bar.get_height())}",
                 ha='center', va='bottom', fontsize=10, color='skyblue')
    for bar in bar2:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{int(bar.get_height())}",
                 ha='center', va='bottom', fontsize=10, color='orange')
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout(rect=[0, 0, 0.85, 1])
    plt.savefig(f"output/{country.lower()}_{brand.lower()}_{year}_prediction.png", bbox_inches='tight')
    plt.show()
    plt.close()

def plot_total_sales_bar(brand, country, year, total_sales):
    plt.figure(figsize=(5, 7))
    bars = plt.bar([f"{brand} {year}"], [total_sales], color='skyblue')
    plt.title(f"Total Sales of {brand} in {country} ({year})")
    plt.ylabel("Units Sold")
    
    for bar in bars:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{int(bar.get_height())}",
                 ha='center', va='bottom', fontsize=10)
    plt.tight_layout(rect=[0, 0, 1, 1])
    plt.show()
    plt.close()
