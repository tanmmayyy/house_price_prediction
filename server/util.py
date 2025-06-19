import json
import pickle
import numpy as np


__locations = None
__data_columns = None
__model = None



def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    
    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __locations


import os

def load_saved_artifacts():
    print("loading saved artifacts...start")
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    global __data_columns, __locations
    
    columns_path = os.path.join(script_dir, "artifacts", "columns.json")
    with open(columns_path, "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]
    
    global __model
    model_path = os.path.join(script_dir, "artifacts", "bengaluru_home_prices_prediction.pickle")
    with open(model_path, "rb") as f:
        __model = pickle.load(f)
    
    print("loading saved artifacts...done")    
    
    
    
    
if __name__ == "__main__":
    
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))  # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))   #