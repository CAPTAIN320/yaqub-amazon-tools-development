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

print(df_csv_file)


# adds a category to ASINs without a category 
df_csv_file["Category"] = df_csv_file["Category"].fillna(top_categories_array[2])


print(df_csv_file)