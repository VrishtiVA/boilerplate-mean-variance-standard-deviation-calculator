import numpy as np

def calculate(list):

    #Checking list contains 9 numbers, otherwise raising ValueError.
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    #Converting into 3x3 NumPy Array
    matrix = np.array(list).reshape((3,3))
    
    #Some settings to use for creating the dictionary.
    properties = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
    operations = ['mean', 'var', 'std', 'max', 'min', 'sum']
    spec_axis = [0, 1, None]

    #Creating Dictionary
    calculations = dict() #or {}

    for index, p in enumerate(properties):
        calculations[p] = [] #Initially Empty Value

        for a in spec_axis:
            calculations[p].append(
                (getattr(matrix, operations[index])(axis=a)).tolist()
            )

    return calculations