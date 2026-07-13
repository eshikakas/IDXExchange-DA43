import pandas as pd

listings_data = pd.read_csv("C:/Users/eshik/IDXExchange/Combined_Listings_Data.csv", low_memory=False)

print(listings_data.columns)
print(listings_data.head(5))

print(listings_data['PropertyType'].unique())

#5 rows and 84 columns

missing_data = pd.DataFrame({
    "Missing Values": listings_data.isnull().sum(),
    "Missing Values Percentage": listings_data.isnull().mean() * 100
})

print(missing_data)
print(missing_data.sort_values("Missing Values Percentage", ascending=False))

filter_out_missing = missing_data[missing_data["Missing Values Percentage"] > 90]
print(filter_out_missing)

columns_to_drop = filter_out_missing.index
listings_data = listings_data.drop(columns=columns_to_drop)

print("New Shape: ", listings_data.shape)
print(listings_data.columns)
#71 columns

# Missing Values  Missing Values Percentage
#FireplacesTotal                       571636                 100.000000
#AboveGradeFinishedArea                571636                 100.000000
#TaxAnnualAmount                       571636                 100.000000
#BuilderName                           545242                  95.382726
#TaxYear                               571636                 100.000000
#BuildingAreaTotal                     521026                  91.146464
#ElementarySchoolDistrict              571636                 100.000000
#CoBuyerAgentFirstName                 557619                  97.547915
#BelowGradeFinishedArea                568393                  99.432681
#BusinessType                          571636                 100.000000
#CoveredSpaces                         571636                 100.000000
#LotSizeDimensions                     541767                  94.774822
#MiddleOrJuniorSchoolDistrict          571636                 100.000000

sold_data = pd.read_csv("C:/Users/eshik/IDXExchange/Combined_sold_Data.csv", low_memory=False)

print(sold_data.columns)
print(sold_data.head(5))

print(sold_data['PropertyType'].unique())

missing_sold_data = pd.DataFrame({
    "Missing Sold Values": sold_data.isnull().sum(),
    "Missing Sold Values Percentage": sold_data.isnull().mean() * 100
})

print(missing_sold_data)
print(missing_sold_data.sort_values("Missing Sold Values Percentage", ascending=False))

filter_out_missing_sold = missing_sold_data[missing_sold_data["Missing Sold Values Percentage"] > 90]
print(filter_out_missing_sold)

columns_to_drop_sold = filter_out_missing_sold.index
sold_data = sold_data.drop(columns=columns_to_drop_sold)

print("New Shape: ", sold_data.shape)
print(sold_data.columns)
#69 columns

#                              Missing Sold Values  Missing Sold Values Percentage
#WaterfrontYN                               430156                       99.937039
#BasementYN                                 421990                       98.039853
#FireplacesTotal                            430427                      100.000000
#AboveGradeFinishedArea                     430427                      100.000000
#TaxAnnualAmount                            430427                      100.000000
#BuilderName                                409358                       95.105093
#TaxYear                                    430427                      100.000000
#BuildingAreaTotal                          400256                       92.990449
#ElementarySchoolDistrict                   430427                      100.000000
#CoBuyerAgentFirstName                      391163                       90.877896
#BelowGradeFinishedArea                     427901                       99.413141
#BusinessType                               430427                      100.000000
#CoveredSpaces                              430427                      100.000000
#LotSizeDimensions                          409528                       95.144589
#MiddleOrJuniorSchoolDistrict               430427                      100.000000

#numeric distribution summary

numeric_columns = ["ClosePrice", "ListPrice", "OriginalListPrice", "LivingArea",
"LotSizeAcres", "BedroomsTotal", "BathroomsTotalInteger", "DaysOnMarket", "YearBuilt"]

for col in numeric_columns:
    print(listings_data[col].describe())

#ClosePrice
#mean     1.208079e+06
#min      5.250000e+02
#50%      8.540000e+05
#max      8.200000e+08

#LivingArea
#mean     1.979705e+03
#min      0.000000e+00
#50%      1.671000e+03
#max      1.702132e+07

#DaysOnMarket
#mean         18.487732
#min         -58.000000
#50%          10.000000
#max        1063.000000

for col in numeric_columns:
    print(sold_data[col].describe())

#ClosePrice
#mean     1.193111e+06
#min      0.000000e+00
#50%      8.250000e+05
#max      9.895000e+08

#LivingArea
#mean     1.904040e+03
#min      0.000000e+00
#50%      1.644000e+03
#max      1.702132e+07

#DaysOnMarket
#mean         37.333513
#min        -288.000000
#50%          18.000000
#max       12430.000000

