# Visualise Function

import matplotlib.pyplot as plt

'''
Python Function to display the count of cars according to the fuel system using a bar chart
'''
def get_cars_fuel_system(df):
    plt.figure()
    df["fuelsystem"].value_counts().plot(kind='bar',color='r') #Plot the bar chart
    plt.ylabel("Counts") #To set y-axis label
    plt.xlabel("Fuel System type") #To set x-axis label
    plt.title("Record of Fuel Systems Per Cars")
    plt.show()
    return

'''
Python Function to display the horsepower of the top 5 cheapest cars using a subplot
'''
def get_hp_top5(df):
    plt.figure()
    car_idx = df.sort_values('price', ascending=True)[:5]["horsepower"].index
    x = df.loc[car_idx]["CarName"].values #Get names of those 5 cars
    y = df.loc[car_idx]["horsepower"].values #Get horsepower of those 5 cars
    plt.bar(x, y) #To plot the bar chart
    plt.xticks(rotation=90) #Rotate x-axis labels
    plt.ylabel("Horsepower") #To set y-axis label
    plt.xlabel("Car") #To set x-axis label
    plt.title("Horsepower of The Top5 Cheapest Cars") 
    plt.show()
    return

'''
Python Function to display the selection of a specified column/feature to visualize the buying behavior of a customer
'''
def get_selected_viz(df, col_name):
    data = df[col_name] #To get the column data
    if data.dtype != 'object': #To check if column is not categorical
        plt.figure()
        data.plot() #Plot the data
        plt.show()
        return
    else: #If the column is categorical
        plt.figure()
        data.value_counts().plot(kind="bar",color='y') #To plot the bar chart of the counts of the data
        plt.show()
        return
        

