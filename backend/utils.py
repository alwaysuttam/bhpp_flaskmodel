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

    print("Location",loc_index)

    a = np.zeros(len(__data_column))
    a[0] = sqft
    a[1] = bath
    a[2] = bhk
    if loc_index >= 0:
        a[loc_index] = 1

    
    return round(__model.predict([a])[0],2)


def get_location_name():
    return __location

def load_model():
    global __location
    global __model
    global __data_column

    with open("data/columns.json", 'r') as f:
        __data_column = json.load(f)['data_columns']
       # print("__data_column ",__data_column)
        __location = __data_column[3:]

    with open("data/banglore_9.pickle", 'rb') as f:
        __model = pickle.load(f)

    print('load model done')

    

if __name__ == '__main__':
    load_model()
    #print(get_location_name())
    
    try:
        price1 = get_estimated_prioce('1st Phase JP Nagar', 1000, 2, 2)
        print("Price for 1st Phase JP Nagar:", price1)
    except Exception as e:
        print("Error predicting price for 1st Phase JP Nagar:", e)
    
    try:
        price2 = get_estimated_prioce('Indira Nagar', 1000, 2, 2)
        print("Price for Indira Nagar:", price2)
    except Exception as e:
        print("Error predicting price for Indira Nagar:", e)
    try:
        price2 = get_estimated_prioce('Whitefield', 1000, 2, 2)
        print("Price for Whitefield:", price2)
    except Exception as e:
        print("Error predicting price for Whitefield:", e)

