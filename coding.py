import glob
import pandas as pd
import numpy as np

pd.set_option('display.max_colwidth', None)


csv_files = glob.glob("categories\*.csv")
current_csv_file = csv_files[4]
current_csv_file = current_csv_file[20:-4]
print(current_csv_file)

# a dictionary of Amazon categories with their corresponding Top-Level category
top_level_categories_dict = {
                        "Appliances": "Appliances",
                        "Beauty & Personal Care": "Beauty & Personal Care",
                        "Clothing, Shoes & Jewelry": "Clothing, Shoes & Jewelry",
                        "Electronics": "Electronics",
                        "Handmade": "Handmade",
                        "Sports & Outdoors": "Sports & Outdoors",
                        "Tools & Home Improvement": "Tools & Home Improvement",
                        "Toys & Games": "Toys & Games",
                        "Card Games": "Toys & Games"
                        }

# a dictionary of Amazon categories with their corresponding Amazon ID
categories_ID_dict = {
                        "Appliances": 2619525011,
                        "Beauty & Personal Care": 3760911,
                        "Clothing, Shoes & Jewelry": 7141123011,
                        "Electronics": 172282,
                        "Handmade": 11260432011,
                        "Sports & Outdoors": 3375251,
                        "Tools & Home Improvement": 228013,
                        "Toys & Games": 165793011,
                        "Card Games": 165793011 # ID same as top category (url issues)
                        }

# convert dictionary into list--------------------maybe not needed since we have dictionary of all Amazon top level categories
#categories_list = list(categories_ID_dict)
#print(categories_list[1])

# convert dictionary values into list
categories_dict_values = categories_ID_dict.values()
categories_list_values = list(categories_dict_values)
print(categories_list_values)


# current category the file is working on
selected_category = top_level_categories_dict[current_csv_file]########### make file names loop inside this, and you will also fix the logic below
print("selected category is", selected_category)

# gets the ID in the categories ID dictionary
selected_category_ID = categories_ID_dict[current_csv_file]


# read the csv file
df_csv_file = pd.read_csv("categories\Brands - " + selected_category + ".csv")

#csv_file = open("categories\Brands - " + selected_category + ".csv", encoding="utf-8")

# retains only ASINs with a Brand
df_csv_file = df_csv_file[df_csv_file["Brand"].notnull()]

# adds a category to ASINs without a category 
df_csv_file["Category"] = df_csv_file["Category"].fillna(selected_category)

# rows with categories that belong to the file
no_of_legit_categories = df_csv_file["Category"].str.contains(selected_category)##################################

# rows with categories that do NOT belong to the file
no_of_illegal_categories = ~df_csv_file["Category"].str.contains(selected_category, na = True)#########################

print("There are", df_csv_file["Category"].count(), "total rows in the file (after removing brandless ASINs)")
print("There are", no_of_legit_categories.sum(), "legitimate rows with the category of", selected_category)
print("There are", no_of_illegal_categories.sum(), "illegal rows in the file")


# data frame with the illegal rows from the file
df_illegal = df_csv_file[no_of_illegal_categories]

# data frame with only the legitimate rows
df_legitimate = df_csv_file[no_of_legit_categories]

# sort legitimate rows according to Top SalesRank
df_legitimate = df_legitimate.sort_values(by=["SalesRank"], ascending=True)

# number of rows where SalesRank = 0
rows_with_zero_SalesRank = df_legitimate["SalesRank"].isin([0])
print("There are", rows_with_zero_SalesRank.sum(), "rows with SalesRank = 0 (pre-removal)")

# retains only rows with a SalesRank > 0
df_legitimate = df_legitimate[df_legitimate["SalesRank"] != 0]

# remove duplicate Brands
df_legitimate = df_legitimate.drop_duplicates(subset=["Brand"])
print("There are", df_legitimate["Brand"].count(), "rows after removing duplicate Brands")


# stores urls of brands
brand_url_array = []
# loop through brand names in the "Brand" column and append
for key, value in df_legitimate["Brand"].iteritems():
    # replace blank spce with a "+" for each brand name
    value = value.replace(" ", "+")
    search_url = "https://www.amazon.com/s?rh=n%3A{}%2Cp_89%3A{}"
    # concatenate category ID and brand names into the url
    brand_URL = search_url.format(categories_ID_dict[selected_category],value)
    # brand_URL = search_url.format(selected_category_ID,value)
    #append brand urls
    brand_url_array.append(brand_URL)

# create column for Brand URLs
df_legitimate["BrandURL"] = brand_url_array


print(df_legitimate)

df_legitimate.to_csv("output.csv")
print("csv file has been generated")

# convert BrandURLs into links
df_legitimate["BrandURL"] = '<a target="_blank" href=' + df_legitimate["BrandURL"] + '><div>' + df_legitimate["Brand"] + '</div></a>'
df_legitimate.to_html("output.html", escape=False)
print("html file has been generated")

