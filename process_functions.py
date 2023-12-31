#!/usr/bin/env python
# coding: utf-8

# Process Function

# In[ ]:


'''
Python to search records by car_ID and return the record
'''
def get_record_by_id(df, car_id):
    car_id_vals = df["car_ID"].values #get all car_ID values
    #Check if car_id is present and valid
    if car_id not in car_id_vals:
        return 0
    else:
        #get the record row by car_id
        record_row = df[df["car_ID"] == car_id].drop("car_ID", axis=1)
        return record_row.T #return the record row
    
'''
Python Function to search and return records with specified number of cylinders
'''
def get_cars_by_cyl(df, cyl_no):
    cyl_no_vals = df["cylindernumber"].values
    #Check if cyl_no is present and valid
    if cyl_no not in cyl_no_vals:
        return 0
    else:
        #Get the records with specified number of cylinders
        result_df = df[df["cylindernumber"] == cyl_no].drop("cylindernumber", axis=1)
        return result_df

'''
Python Function to search and return records with specified body type
'''
def get_cars_by_carbody(df, car_body):
    car_body_vals = df["carbody"].values
    #Check if car_body is present and valid
    if car_body not in car_body_vals:
        return 0
    else:
        #Get the records with specified car body
        result_df = df[df["carbody"] == car_body].drop("carbody", axis=1)
        return result_df
                       
'''
Python Function to get certain columns of a specific car record
'''
def get_record_by_id_columns(df, car_id, col_names):
    record_row = df[df["car_ID"] == car_id] #Get the record row by car_id
    result = record_row[col_names] #Get the columns of the record row
    return result #Return the result

