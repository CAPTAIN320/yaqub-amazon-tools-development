import pandas as pd


top_categories_array = ["Appliances", "Beauty & Personal Care", "Clothing, Shoes & Jewelry", 
                        "Electronics", "Handmade", "Sports & Outdoors", "Tools & Home Improvement",
                        "Toys & Games"]

top_categories_url_dict = {""}

all_categories_array = [""]

top_brands_dict = {

}

df_csv_file = pd.read_csv("categories\Brands - " + top_categories_array[2] + ".csv")

#csv_file = open("categories\Brands - " + top_categories_array[0] + ".csv", encoding="utf-8")


print(df_csv_file[df_csv_file.brand != None])



