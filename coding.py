import pandas as pd
import numpy as np

pd.set_option('display.max_colwidth', None)

# a dictionary of Amazon categories with their Amazon ID
categories_dict = {
                        "Appliances": 2619525011,
                        "Beauty & Personal Care": 3760911,
                        "Clothing, Shoes & Jewelry": 7141123011,
                        "Electronics": 172282,
                        "Handmade": 11260432011,
                        "Sports & Outdoors": 3375251,
                        "Tools & Home Improvement": 228013,
                        "Toys & Games": 165793011}

# convert dictionary to list
categories_list = list(categories_dict)
print(categories_list[1])

# convert dictionary values to list
categories_dict_values = categories_dict.values()
categories_list_values = list(categories_dict_values)


print(categories_list_values)


# current category the file is working on
selected_category = categories_list[5]


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
    brand_URL = search_url.format(categories_dict[selected_category],value)
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