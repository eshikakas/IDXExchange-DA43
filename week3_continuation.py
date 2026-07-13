import pandas as pd

listings = pd.read_csv("C:/Users/eshik/IDXExchange/Cleaned_Combined_Listings_Data.csv", low_memory=False)
sold = pd.read_csv("C:/Users/eshik/IDXExchange/Cleaned_Combined_Sold_Data.csv", low_memory=False)

url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=MORTGAGE30US"

#weekly averages to monthly averages
mortgage = pd.read_csv(url, parse_dates=['observation_date'])
mortgage.columns = ['date', 'rate_30yr_fixed']
mortgage['year_month'] = mortgage['date'].dt.to_period('M')
mortgage_monthly = (mortgage.groupby('year_month')['rate_30yr_fixed'].mean().reset_index())

sold['year_month'] = pd.to_datetime(sold['CloseDate']).dt.to_period('M')
listings['year_month'] = pd.to_datetime(listings['ListingContractDate']).dt.to_period('M')

#merging data to csv
sold_with_rates = sold.merge(mortgage_monthly, on='year_month', how='left')
listings_with_rates = listings.merge(mortgage_monthly, on='year_month', how='left')

#check for unmatched values
print(sold_with_rates['rate_30yr_fixed'].isnull().sum())
print(listings_with_rates['rate_30yr_fixed'].isnull().sum())

print("\nPreview")
print(sold_with_rates[['CloseDate', 'year_month', 'ClosePrice', 'rate_30yr_fixed']].head())

sold_with_rates.to_csv("C:/Users/eshik/IDXExchange/Sold_Data_With_Rates.csv",index=False)
listings_with_rates.to_csv("C:/Users/eshik/IDXExchange/Listings_Data_With_Rates.csv",index=False)