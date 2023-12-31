#Text User Interface Functions

'''
Python Function to display an error message when incorrect option is entered
'''
def display_error():
    print('Incorrect Option Entered! Please try again!!') #To display error message
    
'''
Python Function to display the main option
'''
def display_main_option():
    print("Please Select from option 1-4:")
    user_select = input('''1. Process Data
    \n2. Utilise Data
    \n3. Visualise Data
    \n4. Exit\n''')
    try: #Check if the input is a number
        return int(user_select)
    except: #If the input is not a number
        return 0
    
'''
Python Function to display the process option and process the user's selection
'''
def display_process_option():
    print("Please Select from option 1-4:")
    user_sub_select = input('''1. Retrieve a record for an individual car by ID.
    \n2. Retrieve all cars for a specified cylinder number.
    \n3. Retrieve all cars in the specified car body.
    \n4. Retrieve a specific number of colums(2 to 5), related to an individual car by ID.\n''')
    try: #Check if the input is a number
        return int(user_sub_select)
    except: #If the input is not a number
        return 0

'''
Python Function to display the utilise option and process the user's selection
'''
def display_utilise_option():
    print("Please Select from option 1-4:")
    user_sub_select = input('''1. Retrieve the car names alphabetically.
    \n2. Retrieve summary of sales (total car price) for each car body.
    \n3. Retrieve the top 5 car sale by price (the most expensive) and per car body.
    \n4. Retrieve the detail of cars based on your own selection.\n''')
    try: #Check if the input is a number
        return int(user_sub_select)
    except: #If the input is not a number
        return 0
    
'''
Python Function to display the visualise option and perform visualisations on the data
'''
def display_visualise_option():
    print("Please Select from option 1-3:")
    user_sub_select = input('''1. Display the number of cars per fuel system using a bar chart.
    \n2. Display the horsepower of the top 5 car sale by price (the cheapest) using a subplot.
    \n3. Display the selection of data by your choice to present the customer's buying behavior using a suitable visualisation.\n''')
    try: #Check if the input is a number
        return int(user_sub_select)
    except: #If the input is not a number
        return 0

