import json 
import pickle
import numpy as np


__location = None
__model = None
__data_column = None

def get_estimated_prioce(location,sqft,bhk,bath):

    try:
        loc_index = __data_column.index(location.lower())
    except :
        loc_index = -1

    x = np.zeros(len(__data_column))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    
    return __model.predict([x])[0]

def get_location_name():
    return __location

def load_model():
    global __location
    global __model
    global __data_column

    with open("data/columns.json", 'r') as f:
        __data_column = json.load(f)['data_columns']
        print("__data_column jkxgj jkxgvu",__data_column)
        __location = __data_column[3:]

    with open("data/bhpp_v2.pickle", 'rb') as f:
        __model = pickle.load(f)

    print('load model done')

    

if __name__ == '__main__':
    load_model()
    print(get_location_name())
    get_estimated_prioce('Indira Nagar',1000,3,3)
    get_estimated_prioce('1st Phase JP Nagar',1000,3,3)
