import pandas as pd
import numpy as np

# an array of top amazon categories
top_categories_array = ["Appliances", "Beauty & Personal Care", "Clothing, Shoes & Jewelry", 
                        "Electronics", "Handmade", "Sports & Outdoors", "Tools & Home Improvement",
                        "Toys & Games"]

# an array of the urls of top amazon categories
top_categories_url_dict = {""}

# an array of all the categories that were scanned using ZonAsin
all_scanned_categories_array = [""]

top_brands_dict = {

}

# read the csv file
df_csv_file = pd.read_csv("categories\Brands - " + top_categories_array[2] + ".csv")

#csv_file = open("categories\Brands - " + top_categories_array[0] + ".csv", encoding="utf-8")


# removes all ASINs without a brand
df_csv_file = df_csv_file[df_csv_file["Brand"].notnull()]


# adds a category to ASINs without a category 
df_csv_file["Category"] = df_csv_file["Category"].fillna(top_categories_array[2])


# rows that belong to the file (i.e. the majo)
no_of_legit_categories = df_csv_file["Category"].str.contains(top_categories_array[2])

# rows that do NOT belong to the file
no_of_illegal_categories = ~df_csv_file["Category"].str.contains(top_categories_array[2], na = True)

print("There are", df_csv_file["Category"].count(), "total rows in the file")
print("There are", no_of_legit_categories.sum(), "legitimate rows with the category of", top_categories_array[2])
print("There are", no_of_illegal_categories.sum(), " illegal rows in the file")

# data frame with only the categories that belong to file
df_csv_file = df_csv_file[no_of_legit_categories]

df_illegal_csv_file = no_of_illegal_categories

print(no_of_illegal_categories.sum())