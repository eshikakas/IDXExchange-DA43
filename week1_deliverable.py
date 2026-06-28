import pandas as pd
import os
import glob

folder = "C:/Users/eshik/IDXExchange"
listing_files = sorted(glob.glob(os.path.join(folder, "CRMLSListing*.csv")))
listing_dfs = []

for listing_file in listing_files:
    df = pd.read_csv(listing_file, low_memory = False)
    listing_dfs.append(df)

#Listing row count before concatenation 
listing_rows_before_concat = sum(len(df) for df in listing_dfs)
print("Listings before concatenation: ", listing_rows_before_concat)

#Combined listing DataFrames
combined_listings_df = pd.concat(listing_dfs, ignore_index=True)

#Row count before Residential filtering
listings_before_filter = len(combined_listings_df)
print("Listings before Residential filter: ", listings_before_filter)

combined_listings_df = combined_listings_df[combined_listings_df["PropertyType"] == "Residential"]

#Row count after Residential filtering
listings_after_filter = len(combined_listings_df)

print("Listings after Residential filter: ", listings_after_filter)

listing_csv = os.path.join(folder, "Combined_Listings.csv")
combined_listings_df.to_csv(listing_csv, index=False)

#Retrieving sold files
sold_files = sorted(glob.glob(os.path.join(folder, "CRMLSSold*.csv")))
sold_dfs = []

for sold_file in sold_files:
    df = pd.read_csv(sold_file, low_memory = False)
    sold_dfs.append(df)

#Sold row count before concatenation 
sold_rows_before_concat = sum(len(df) for df in sold_dfs)
print("Sold before concatenation: ", sold_rows_before_concat)

#Combined sold DataFrames
combined_sold_df = pd.concat(sold_dfs, ignore_index=True)

#Row count before Residential filtering
Sold_before_filter = len(combined_sold_df)
print("Sold before Residential filter: ", Sold_before_filter)

combined_sold_df = combined_sold_df[combined_sold_df["PropertyType"] == "Residential"]

#Row count after Residential filtering
sold_after_filter = len(combined_sold_df)

print("Sold after Residential filter: ", sold_after_filter)

sold_csv = os.path.join(folder, "Combined_Sold.csv")
combined_sold_df.to_csv(sold_csv, index=False)

#Listings before concatenation:  897663
#Listings before Residential filter:  897663
#Listings after Residential filter:  571636
#Sold before concatenation:  705749
#Sold before Residential filter:  705749
#Sold after Residential filter:  474709
