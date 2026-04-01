from sklearn.linear_model import LinearRegression
import numpy as np

def get_top_per_country_year(df):
    return (
        df.sort_values(['year', 'country', 'sales'], ascending=[True, True, False])
          .groupby(['year', 'country'], as_index=False)
          .first()
          .rename(columns={'brand': 'top_brand', 'sales': 'top_sales'})
    )

def get_global_top(top_per_country_year):
    return (
        top_per_country_year.groupby(['year', 'top_brand'])
                            .size().reset_index(name='countries_count')
                            .sort_values(['year', 'countries_count'], ascending=[True, False])
                            .groupby('year').first().reset_index()
    )

def get_total_sales(df, country, brand, year):
    result = df[(df['country'] == country) & (df['brand'] == brand) & (df['year'] == year)]
    if not result.empty:
        return result['sales'].iloc[0]
    return None

def get_comparison_data(df, countries, brands, years):
    filtered = df[
        df['country'].isin(countries) &
        df['brand'].isin(brands) &
        df['year'].isin(years)
    ]
    plot_data = []
    for country in countries:
        for brand in brands:
            for year in years:
                row = filtered[
                    (filtered['country'] == country) &
                    (filtered['brand'] == brand) &
                    (filtered['year'] == year)
                ]
                sales = row['sales'].iloc[0] if not row.empty else 0
                plot_data.append({'Country': country, 'Brand': brand, 'Year': year, 'Sales': sales})
    return plot_data

def predict_sales(df, country, brand, year): 
    data = df[(df['country'] == country) & (df['brand'] == brand)]
    if data.empty or data['year'].nunique() < 2:
        return None

    X = data['year'].values.reshape(-1, 1)
    y = data['sales'].values
    model = LinearRegression()
    model.fit(X, y)
    predicted = model.predict(np.array([[year]]))
    return int(predicted[0])
