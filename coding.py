import pandas as pd
import numpy as np

#pd.set_option('display.max_rows', None)

# an array of top amazon categories
top_categories_array = ["Appliances", "Beauty & Personal Care", "Clothing, Shoes & Jewelry", 
                        "Electronics", "Handmade", "Sports & Outdoors", "Tools & Home Improvement",
                        "Toys & Games"]

# an dictionary Amazon categories with their Amazon ID
categories_dict = {
                        "Appliances": 2619525011,
                        "Beauty & Personal Care": 3760911,
                        "Clothing, Shoes & Jewelry": 7141123011,
                        "Electronics": 172282,
                        "Handmade": 11260432011,
                        "Sports & Outdoors": 3375251,
                        "Tools & Home Improvement": 228013,
                        "Toys & Games": 165793011
            }


# an array of all the categories that were scanned using ZonAsin
all_scanned_categories_array = [""]

top_brands_dict = {

}

selected_category = top_categories_array[1]

# read the csv file
df_csv_file = pd.read_csv("categories\Brands - " + selected_category + ".csv")

#csv_file = open("categories\Brands - " + selected_category + ".csv", encoding="utf-8")

# removes all ASINs without a brand
df_csv_file = df_csv_file[df_csv_file["Brand"].notnull()]

# adds a category to ASINs without a category 
df_csv_file["Category"] = df_csv_file["Category"].fillna(selected_category)

# rows with categories that belong to the file
no_of_legit_categories = df_csv_file["Category"].str.contains(selected_category)

# rows with categories that do NOT belong to the file
no_of_illegal_categories = ~df_csv_file["Category"].str.contains(selected_category, na = True)

print("There are", df_csv_file["Category"].count(), "total rows in the file (after removing brandless ASINs)")
print("There are", no_of_legit_categories.sum(), "legitimate rows with the category of", selected_category)
print("There are", no_of_illegal_categories.sum(), "illegal rows in the file")


# data frame with the illegal rows from the file
df_illegal = df_csv_file[no_of_illegal_categories]

# data frame with only the legitimate rows
df_legitimate = df_csv_file[no_of_legit_categories]

# sort legitimate rows according to Top SalesRank
df_legitimate = df_legitimate.sort_values(by=["SalesRank"], ascending=True)

# remove duplicate Brands
df_legitimate = df_legitimate.drop_duplicates(subset=["Brand"])
print("There are", df_legitimate["Brand"].count(), "rows after removing duplicate Brands")

# number of rows where SalesRank = 0
rows_with_zero_SalesRank = df_legitimate["SalesRank"].isin([0])
print("There are", rows_with_zero_SalesRank.sum(), "rows with SalesRank = 0")

print(df_legitimate)

