import glob
import logging
import pandas as pd

pd.set_option('display.max_colwidth', None)

# logger creation and configuration
logging.basicConfig(filename="std.log", 
					format='%(asctime)s %(message)s', 
					filemode='w')

# creating object
logger = logging.getLogger()

# set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG)

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
                        "Office Products": "Office Products",
                        "Women Hand Bags & Wallets": "Clothing, Shoes & Jewelry",
                        "Women Jewelry": "Clothing, Shoes & Jewelry",
                        "Men Jewelry": "Clothing, Shoes & Jewelry",
                        "Girl Jewelry": "Clothing, Shoes & Jewelry",
                        "Boy Jewelry": "Clothing, Shoes & Jewelry",
                        "Power Tools": "Tools & Home Improvement",
                        "Boy Hoodies": "Clothing, Shoes & Jewelry",
                        "Men Hoodies": "Clothing, Shoes & Jewelry",
                        "Men Jackets": "Clothing, Shoes & Jewelry",
                        "Women Hoodies": "Clothing, Shoes & Jewelry",
                        "Girl Hoodies": "Clothing, Shoes & Jewelry",
                        "Men Watches": "Clothing, Shoes & Jewelry",
                        "Men Bags": "Clothing, Shoes & Jewelry",
                        "Men Wallets": "Clothing, Shoes & Jewelry",
                        "Women Watches": "Clothing, Shoes & Jewelry",
                        "Women Wallets": "Clothing, Shoes & Jewelry",
                        "Card Games": "Toys & Games",
                        "Board Games": "Toys & Games",
                        "Women Pumps (shoes)": "Clothing, Shoes & Jewelry",
                        "Women Flats (shoes)": "Clothing, Shoes & Jewelry",
                        "Women Boots (shoes)": "Clothing, Shoes & Jewelry",
                        "Women Loafers (shoes)": "Clothing, Shoes & Jewelry",
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
                        "Office Products": 1064954,
                        "Women Hand Bags & Wallets": 15743631,
                        "Women Jewelry": 7192394011,
                        "Men Jewelry": 3887881,
                        "Girl Jewelry": 3880961,
                        "Boy Jewelry": 3880611,
                        "Power Tools": 551236,
                        "Boy Hoodies": 5604815011,
                        "Men Hoodies": 1258644011,
                        "Men Jackets": 1045830,
                        "Women Hoodies": 1258603011,
                        "Girl Hoodies": 5604818011,
                        "Men Watches": 6358539011,
                        "Men Bags": 14864589011,
                        "Men Wallets": 7072333011,
                        "Women Watches": 6358543011,
                        "Women Wallets": 7072326011,
                        "Card Games": 165793011, # ID same as top category (url issues)
                        "Board Games": 166225011,
                        "Women Pumps (shoes)": 679416011,
                        "Women Flats (shoes)": 679399011,
                        "Women Boots (shoes)": 679380011,
                        "Women Loafers (shoes)": 679404011,
                        }

# convert categories ID dictionary values into list
categories_ID_list = list(categories_ID_dict.values())



csv_files = glob.glob("categories\*.csv")

# an array of the csv files in the folder
current_files_array = []
logger.info("The CSV files are")
# loop to create array of current csv files found in the folder
for file in csv_files:
    file = file[20:-4]
    current_files_array.append(file)
    logger.info(file)


print("KEEP CALM, Program is running :)")
logger.info("")


# loops through every csv file found
for current_file in current_files_array:

    # category of the current file
    current_category = top_level_categories_dict[current_file]
    #print("Current category is", current_category)
    logger.info("Current file is "+current_file)
    logger.info("Current category is "+current_category)

    # gets the ID in the categories ID dictionary
    selected_category_ID = categories_ID_dict[current_file]


    # read the csv file
    df_csv_file = pd.read_csv(
        "categories\Brands - " + current_category + ".csv", 
        dtype={"ASIN": "string", "Brand": "string", "Category": "string", "SalesRank": int}
        )

    # retains only ASINs with a Brand
    df_csv_file = df_csv_file[df_csv_file["Brand"].notnull()]

    # adds a category to ASINs without a category 
    df_csv_file["Category"] = df_csv_file["Category"].fillna(current_category)

    # rows with categories that belong to the file
    no_of_legit_categories = df_csv_file["Category"].str.contains(current_category)##################################

    # rows with categories that do NOT belong to the file
    no_of_illegal_categories = ~df_csv_file["Category"].str.contains(current_category, na = True)#########################

    #print("There are", df_csv_file["Category"].count(), "total rows in the file (after removing brandless ASINs)")
    #print("There are", no_of_legit_categories.sum(), "legitimate rows with the category of", current_category)
    #print("There are", no_of_illegal_categories.sum(), "illegal rows in the file")


    # data frame with the illegal rows from the file
    df_illegal = df_csv_file[no_of_illegal_categories]

    # data frame with only the legitimate rows
    df_legitimate = df_csv_file[no_of_legit_categories]

    # sort legitimate rows according to Top SalesRank
    df_legitimate = df_legitimate.sort_values(by=["SalesRank"], ascending=True)

    # number of rows where SalesRank = 0
    #rows_with_zero_SalesRank = df_legitimate["SalesRank"].isin([0])
    #print("There are", rows_with_zero_SalesRank.sum(), "rows with SalesRank = 0 (pre-removal)")

    # retains only rows with a SalesRank > 0
    df_legitimate = df_legitimate[df_legitimate["SalesRank"] != 0]

    # remove duplicate Brands
    df_legitimate = df_legitimate.drop_duplicates(subset=["Brand"])
    #print("There are", df_legitimate["Brand"].count(), "rows after removing duplicate Brands")


    # stores urls of brands
    brand_url_array = []
    # loop through brand names in the "Brand" column and append
    for key, value in df_legitimate["Brand"].iteritems():
        # replace blank spce with a "+" for each brand name
        value = value.replace(" ", "+")
        search_url = "https://www.amazon.com/s?rh=n%3A{}%2Cp_89%3A{}"
        # concatenate category ID and brand names into the url
        brand_URL = search_url.format(selected_category_ID,value)
        #append brand urls
        brand_url_array.append(brand_URL)

    # create column for Brand URLs
    df_legitimate["BrandURL"] = brand_url_array

    # generate new csv file
    df_legitimate.to_csv("filtered_csv\\"+current_file+".csv")
    #print(current_file+" csv file has been generated")
    logger.info(current_file+" csv file has been generated")

    # convert BrandURLs into links
    df_legitimate["BrandURL"] = '<a target="_blank" href=' + df_legitimate["BrandURL"] + '><div>' + df_legitimate["Brand"] + '</div></a>'
    # generate csv file
    df_legitimate.to_html("html\\"+current_file+".html", escape=False)
    #print(current_file+" html file has been generated")
    logger.info(current_file+" html file has been generated")
    #print()
    logger.info("")


print("\nFinished. Check the log for more info")
