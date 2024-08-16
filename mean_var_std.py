import numpy as np

def calculate(list):

    #Checking list contains 9 numbers, otherwise raising ValueError.
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    #Converting into 3x3 NumPy Array
    matrix = np.array(list).reshape((3,3))
    
    #Creating Dictionary
    properties = ['mean', 'var', 'std', 'max', 'min', 'sum']
    operations = [0, 1, None]
    calculations = dict() #or {}

    for p in properties:
        calculations[p] = [] #Initially Empty Value

        for o in operations:
            calculations[p].append(
                (getattr(matrix, p)(axis=o)).tolist()
            )

    return calculations