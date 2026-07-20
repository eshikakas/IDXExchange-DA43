import pandas as pd

listings = pd.read_csv("C:/Users/eshik/IDXExchange/Listings_Data_With_Rates.csv", low_memory=False)
sold = pd.read_csv("C:/Users/eshik/IDXExchange/Sold_Data_With_Rates.csv", low_memory=False)

#convert to datetime format
date_fields = ["CloseDate", "PurchaseContractDate", "ListingContractDate", "ContractStatusChangeDate"]

for col in date_fields:
    if col in listings.columns:
        listings[col] = pd.to_datetime(listings[col])
    if col in sold.columns:
        sold[col] = pd.to_datetime(sold[col])

#ensure numeric fields are properly typed
numeric_fields = ["ClosePrice", "LivingArea", "DaysOnMarket", "ListPrice", "OriginalListPrice", "BedroomsTotal", "BathroomsTotalInteger", "LotSizeAcres"]

for col in numeric_fields:
    if col in listings.columns:
        listings[col] = pd.to_numeric(listings[col])
    if col in sold.columns:
        sold[col] = pd.to_numeric(sold[col])

#flag invalid listings data
listings["invalid_closeprice"] = listings["ClosePrice"] <= 0
listings["invalid_livingarea"] = listings["LivingArea"] <= 0
listings["invalid_daysonmarket"] = listings["DaysOnMarket"] <= 0
listings["invalid_listprice"] = listings["ListPrice"] <= 0
listings["invalid_originallistprice"] = listings["OriginalListPrice"] <= 0
listings["invalid_bedroomstotal"] = listings["BedroomsTotal"] <= 0
listings["invalid_bathroomstotal"] = listings["BathroomsTotalInteger"] <= 0
listings["invalid_lotsizeacres"] = listings["LotSizeAcres"] <= 0

print("\nInvalid Listing Values:")
print("Invalid ClosePrice:", listings["invalid_closeprice"].sum())
print("Invalid LivingArea:", listings["invalid_livingarea"].sum())
print("Invalid DaysOnMarket:", listings["invalid_daysonmarket"].sum())
print("Invalid ListPrice:", listings["invalid_listprice"].sum())
print("Invalid OriginalListPrice:", listings["invalid_originallistprice"].sum())
print("Invalid BedroomsTotal:", listings["invalid_bedroomstotal"].sum())
print("Invalid BathroomsTotalInteger:", listings["invalid_bathroomstotal"].sum())
print("Invalid LotSizeAcres:", listings["invalid_lotsizeacres"].sum())

#Invalid Listing Values:
#Invalid ClosePrice: 0
#Invalid LivingArea: 374
#Invalid DaysOnMarket: 31412
#Invalid ListPrice: 0
#Invalid OriginalListPrice: 4
#Invalid BedroomsTotal: 2258
#Invalid BathroomsTotalInteger: 711
#Invalid LotSizeAcres: 12488

#flag invalid sold data
sold["invalid_closeprice"] = sold["ClosePrice"] <= 0
sold["invalid_livingarea"] = sold["LivingArea"] <= 0
sold["invalid_daysonmarket"] = sold["DaysOnMarket"] <= 0
sold["invalid_listprice"] = sold["ListPrice"] <= 0
sold["invalid_originallistprice"] = sold["OriginalListPrice"] <= 0
sold["invalid_bedroomstotal"] = sold["BedroomsTotal"] <= 0
sold["invalid_bathroomstotal"] = sold["BathroomsTotalInteger"] <= 0
sold["invalid_lotsizeacres"] = sold["LotSizeAcres"] <= 0

print("\nInvalid Sold Values:")
print("Invalid ClosePrice:", sold["invalid_closeprice"].sum())
print("Invalid LivingArea:", sold["invalid_livingarea"].sum())
print("Invalid DaysOnMarket:", sold["invalid_daysonmarket"].sum())
print("Invalid ListPrice:", sold["invalid_listprice"].sum())
print("Invalid OriginalListPrice:", sold["invalid_originallistprice"].sum())
print("Invalid BedroomsTotal:", sold["invalid_bedroomstotal"].sum())
print("Invalid BathroomsTotalInteger:", sold["invalid_bathroomstotal"].sum())
print("Invalid LotSizeAcres:", sold["invalid_lotsizeacres"].sum())

#Invalid Sold Values:
#Invalid ClosePrice: 1
#Invalid LivingArea: 153
#Invalid DaysOnMarket: 17331
#Invalid ListPrice: 0
#Invalid OriginalListPrice: 2
#Invalid BedroomsTotal: 1221
#Invalid BathroomsTotalInteger: 326
#Invalid LotSizeAcres: 9002