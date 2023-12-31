# Utilise Function


'''
Python Function to get all the car names, in alphabetical order
'''
def get_car_name_alpha(df):
    return df["CarName"].str.lower().sort_values() #Return car names in sorted order

'''
Python Function to retrieve summary of sales (total car price) for each car body
'''
def get_car_body_total_price(df):
    return df.groupby("carbody")["price"].sum() #Return car body total price sum

'''
Python Function to retrieve the top 5 cars by price and per car body
'''
def get_car_body_total_top5(df):
    return df.groupby("carbody")["price"].nlargest(5) #Return top 5 cars of each body type

'''
Python Function to retrieve selected data of a column
'''
def get_selected_data(df, col_name, value):
    result = df[df[col_name] == value] #Get the records with specified value
    return result

