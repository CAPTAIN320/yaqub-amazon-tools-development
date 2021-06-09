import glob
import logging
import pandas as pd
import itertools

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
                        # "Category": [US_category_ID, JP_category_ID] 0 = no ID
                        "Appliances": [2619525011, 124048011],
                        "Beauty & Personal Care": [3760911, 52374051],
                        "Clothing, Shoes & Jewelry": [7141123011, 352484011],
                        "Electronics": [172282, 3210981],
                        "Handmade": [11260432011, 0],
                        "Sports & Outdoors": [3375251, 14304371],
                        "Tools & Home Improvement": [228013, 2016929051],
                        "Toys & Games": [165793011, 13299531],
                        "Musical Instruments": [11091801, 2123629051],
                        "Office Products": [1064954, 86731051],
                        "Women Hand Bags & Wallets": [15743631, 2221075051],
                        "Women Jewelry": [7192394011, 5519723051],
                        "Men Jewelry": [3887881, 86246051],
                        "Girl Jewelry": [3880961, 0],
                        "Boy Jewelry": [3880611, 0],
                        "Power Tools": [551236, 0],
                        "Boy Hoodies": [5604815011, 2131573051],
                        "Men Hoodies": [1258644011, 2131434051],
                        "Men Jackets": [1045830, 2131419051],
                        "Women Hoodies": [1258603011, 2131504051],
                        "Girl Hoodies": [5604818011, 0],
                        "Men Watches": [6358539011, 333009011],
                        "Men Bags": [14864589011, 5355946051],
                        "Men Wallets": [7072333011, 2221209051],
                        "Women Watches": [6358543011, 333010011],
                        "Women Bags": [0, 5355945051],
                        "Women Wallets": [7072326011, 2221186051],
                        "Card Games": [166239011, 0],
                        "Board Games": [166225011, 0],
                        "Women Pumps (shoes)": [679416011, 2221092051],
                        "Women Flats (shoes)": [679399011, 0],
                        "Women Boots (shoes)": [679380011, 2221085051],
                        "Women Loafers (shoes)": [679404011, 2221090051],
                        "Jewelry Accessories": [9616098011, 86252051],
                        "Puzzles": [0, 2189596051],
                        "Building Toys": [0, 2189163051],
                        "Sports & Outdoor Play": [0, 2189318051],
                        "Necklaces & Pendants": [0, 86228051],
                        "Stuffed Animals & Plush Toys": [166461011, 2189188051]
                        }

# convert categories ID dictionary values into list
# categories_ID_list = list(categories_ID_dict.values())

# print(categories_ID_list[0][0])  # this is how to access second one



csv_files_US = glob.glob("categories\*.csv")

csv_files_JP = glob.glob("categories_JP\*.csv")



""" # loop to create array of current csv files found in the folder
for file_US in csv_files_US:
    file_US = file_US[20:-4]
    current_US_files_array.append(file_US)
    logger.info(file_US)

current_JP_files_array = []
for file_JP in csv_files_JP:
    file_JP = file_JP[26:-4]
    current_JP_files_array.append(file_US)
    logger.info(file_US) """

# an array of the csv files in categories their respective folders
current_US_files_array = []
current_JP_files_array = []
# loop to create array of current csv files found in their respective folders
for file_US, file_JP in itertools.product(csv_files_US, csv_files_JP):
    file_US = file_US[20:-4]
    file_JP = file_JP[26:-4]
    
    current_US_files_array.append(file_US)
    current_JP_files_array.append(file_JP)

logger.info("The US CSV files are")
logger.info(current_US_files_array)

logger.info("The JP CSV files are")
logger.info(current_JP_files_array)

print("KEEP CALM, Program is running :)")
logger.info("")

""" for current_US_file, current_JP_file in itertools.product(current_US_files_array, current_JP_files_array):
    print (current_US_file, "\n"+current_JP_file) """

# loops through every csv file_US found in categories US folder
for current_US_file in current_US_files_array:
    
    
    # gets the ID of Amazon JP in the categories ID dictionary
    selected_US_category_ID = categories_ID_dict[current_US_file][0]
    selected_JP_category_ID = categories_ID_dict[current_US_file][1]

    """ 
    # checks if a file_US has an Amazon US ID
    if bool(selected_US_category_ID) == True: 
        print("this is an if stmnt")
     """    
    
    # category of the current file_US
    current_category = top_level_categories_dict[current_US_file]
    #print("Current category is", current_category)
    logger.info("Current file_US is "+current_US_file)
    logger.info("Current category is "+current_category)

    # read the csv file_US
    df_csv_file = pd.read_csv(
        "categories\Brands - " + current_US_file + ".csv", 
        dtype={"ASIN": "string", "Brand": "string", "Category": "string", "SalesRank": int}
        )

    # retains only ASINs with a Brand
    df_csv_file = df_csv_file[df_csv_file["Brand"].notnull()]

    # adds a category to ASINs without a category 
    df_csv_file["Category"] = df_csv_file["Category"].fillna(current_category)

    # rows with categories that belong to the file_US
    no_of_legit_categories = df_csv_file["Category"].str.contains(current_category)

    # rows with categories that do NOT belong to the file_US
    no_of_illegal_categories = ~df_csv_file["Category"].str.contains(current_category, na = True)

    #print("There are", df_csv_file["Category"].count(), "total rows in the file_US (after removing brandless ASINs)")
    #print("There are", no_of_legit_categories.sum(), "legitimate rows with the category of", current_category)
    #print("There are", no_of_illegal_categories.sum(), "illegal rows in the file_US")


    # data frame with the illegal rows from the file_US
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
    us_brand_url_array = []
    jp_brand_url_array = []
    ali_brand_url_array = []
    gogl_brand_url_array = []
    # loop through brand names in the "Brand" column and append
    for key, value in df_legitimate["Brand"].iteritems():
        # replace blank spce with a "+" for each brand name
        value = value.replace(" ", "+")
        # create the urls
        us_search_url = "https://www.amazon.com/s?rh=n%3A{}%2Cp_89%3A{}"
        jp_search_url = "https://www.amazon.co.jp/s?rh=n%3A{}%2Cp_89%3A{}"
        ali_search_url = "https://www.aliexpress.com/af/{}.html"
        gogl_search_URL = "https://www.google.com/search?q={}"
        # concatenate category ID and brand names into the url
        us_brand_URL = us_search_url.format(selected_US_category_ID,value)
        jp_brand_URL = jp_search_url.format(selected_JP_category_ID,value)
        ali_brand_URL = ali_search_url.format(value)
        gogl_search_URL = gogl_search_URL.format(value)
        #append brand urls
        us_brand_url_array.append(us_brand_URL)
        jp_brand_url_array.append(jp_brand_URL)
        ali_brand_url_array.append(ali_brand_URL)
        gogl_brand_url_array.append(gogl_search_URL)

    # create column for Brand URLs
    df_legitimate["US_BrandURL"] = us_brand_url_array
    df_legitimate["JP_BrandURL"] = jp_brand_url_array
    df_legitimate["AliBrandURL"] = ali_brand_url_array
    df_legitimate["GoglBrandURL"] = gogl_brand_url_array

    # generate new csv file_US
    df_legitimate.to_csv("filtered_csv\\"+current_US_file+".csv")
    #print(current_US_file+" csv file_US has been generated")
    logger.info(current_US_file+" csv file_US has been generated")

    # convert BrandURLs into links
    df_legitimate["US_BrandURL"] = '<a target="_blank" href=' + df_legitimate["US_BrandURL"] + '><div>' + df_legitimate["Brand"] + '</div></a>'
    df_legitimate["JP_BrandURL"] = '<a target="_blank" href=' + df_legitimate["JP_BrandURL"] + '><div>' + df_legitimate["Brand"] + '</div></a>'
    df_legitimate["AliBrandURL"] = '<a target="_blank" href=' + df_legitimate["AliBrandURL"] + '><div>' + df_legitimate["Brand"] + '</div></a>'
    df_legitimate["GoglBrandURL"] = '<a target="_blank" href=' + df_legitimate["GoglBrandURL"] + '><div>' + df_legitimate["Brand"] + '</div></a>'
    
    # generate csv file_US
    df_legitimate.to_html("html\\"+current_US_file+".html", escape=False)
    
    #print(current_US_file+" html file_US has been generated")
    logger.info(current_US_file+" html file_US has been generated")
    #print()
    logger.info("")



print("\nFinished for USA categories.\nNow doing Japanese categories")

# loops through every csv file_JP found in categories JP folder
for current_JP_file in current_JP_files_array:
    
    
    # gets the ID of Amazon JP in the categories ID dictionary
    selected_US_category_ID = categories_ID_dict[current_JP_file][0]
    selected_JP_category_ID = categories_ID_dict[current_JP_file][1]

    """ 
    # checks if a file_JP has an Amazon JP ID
    if bool(selected_JP_category_ID) == True: 
        print("this is an if stmnt")
    """    
    
    # category of the current file_JP
    current_JP_category = top_level_categories_dict[current_JP_file]
    #print("Current category is", current_JP_category)
    logger.info("Current file_JP is "+current_JP_file)
    logger.info("Current category is "+current_JP_category)




    # read the csv file_JP
    df_csv_file = pd.read_csv(
        "categories_JP\JP Brands - " + current_JP_file + ".csv", 
        dtype={"ASIN": "string", "Brand": "string", "Category": "string", "SalesRank": int}
        )

    # retains only ASINs with a Brand
    df_csv_file = df_csv_file[df_csv_file["Brand"].notnull()]

    # adds a category to ASINs without a category 
    df_csv_file["Category"] = df_csv_file["Category"].fillna(current_JP_category)

    # rows with categories that belong to the file_JP
    no_of_legit_categories = df_csv_file["Category"].str.contains(current_JP_category)

    # rows with categories that do NOT belong to the file_JP
    no_of_illegal_categories = ~df_csv_file["Category"].str.contains(current_JP_category, na = True)

    #print("There are", df_csv_file["Category"].count(), "total rows in the file_JP (after removing brandless ASINs)")
    #print("There are", no_of_legit_categories.sum(), "legitimate rows with the category of", current_JP_category)
    #print("There are", no_of_illegal_categories.sum(), "illegal rows in the file_JP")


    # data frame with the illegal rows from the file_JP
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
    us_brand_url_array = []
    jp_brand_url_array = []
    ali_brand_url_array = []
    gogl_brand_url_array = []
    # loop through brand names in the "Brand" column and append
    for key, value in df_legitimate["Brand"].iteritems():
        # replace blank spce with a "+" for each brand name
        value = value.replace(" ", "+")
        # create the urls
        us_search_url = "https://www.amazon.com/s?rh=n%3A{}%2Cp_89%3A{}"
        jp_search_url = "https://www.amazon.co.jp/s?rh=n%3A{}%2Cp_89%3A{}"
        ali_search_url = "https://www.aliexpress.com/af/{}.html"
        gogl_search_URL = "https://www.google.com/search?q={}"
        # concatenate category ID and brand names into the url
        us_brand_URL = us_search_url.format(selected_US_category_ID,value)
        jp_brand_URL = jp_search_url.format(selected_JP_category_ID,value)
        ali_brand_URL = ali_search_url.format(value)
        gogl_search_URL = gogl_search_URL.format(value)
        #append brand urls
        us_brand_url_array.append(us_brand_URL)
        jp_brand_url_array.append(jp_brand_URL)
        ali_brand_url_array.append(ali_brand_URL)
        gogl_brand_url_array.append(gogl_search_URL)

    # create column for Brand URLs
    df_legitimate["US_BrandURL"] = us_brand_url_array
    df_legitimate["JP_BrandURL"] = jp_brand_url_array
    df_legitimate["AliBrandURL"] = ali_brand_url_array
    df_legitimate["GoglBrandURL"] = gogl_brand_url_array

    # generate new csv file_JP
    df_legitimate.to_csv("filtered_csv\\JP - "+current_JP_file+".csv")
    #print(current_JP_file+" csv file_JP has been generated")
    logger.info(current_JP_file+" csv file_JP has been generated")

    # convert BrandURLs into links
    df_legitimate["US_BrandURL"] = '<a target="_blank" href=' + df_legitimate["US_BrandURL"] + '><div>' + df_legitimate["Brand"] + '</div></a>'
    df_legitimate["JP_BrandURL"] = '<a target="_blank" href=' + df_legitimate["JP_BrandURL"] + '><div>' + df_legitimate["Brand"] + '</div></a>'
    df_legitimate["AliBrandURL"] = '<a target="_blank" href=' + df_legitimate["AliBrandURL"] + '><div>' + df_legitimate["Brand"] + '</div></a>'
    df_legitimate["GoglBrandURL"] = '<a target="_blank" href=' + df_legitimate["GoglBrandURL"] + '><div>' + df_legitimate["Brand"] + '</div></a>'
    
    # generate csv file_JP
    df_legitimate.to_html("html\\JP - "+current_JP_file+".html", escape=False)
    
    #print(current_JP_file+" html file_JP has been generated")
    logger.info(current_JP_file+" html file_JP has been generated")
    
    #print()
    logger.info("")



print("\nFinished. Check the log for more info")
