import pandas as pd
from sklearn import linear_model
import numpy as np
from app.database.database_connection import DatabaseConnection
import pickle
import base64

class MultipleRegression: 
    def __init__(self):
        self.regr = None    

    def trainModelForUser(self, userName : str):
        
        print(f"Train model for {userName}")
        databaseConnection = DatabaseConnection()
        
        runs = databaseConnection.getAllRunsByUser(userName)
        
        data = {
            'top_field': [],
            'bottom_field': [],
            'right_field': [],
            'left_field': [],
            'center_field': [],
            'lose_count': [],
        }
        
        for run in runs:
            data['top_field'].append(run[0])
            data['bottom_field'].append(run[1])
            data['right_field'].append(run[2])
            data['left_field'].append(run[3])
            data['center_field'].append(run[4])
            data['lose_count'].append(run[5])

        if (len(data['top_field']) == 0):
            return

        df = pd.DataFrame(data)

        x = df[['top_field','bottom_field', 'right_field', 'left_field', 'center_field']]
        y = df['lose_count']
        
        # with sklearn
        regr = linear_model.LinearRegression()
        regr.fit(x.values, y)

        # print('Intercept: \n', regr.intercept_)
        # print('Coefficients: \n', regr.coef_)
        
        self.regr = regr
        
        databaseConnection.updateUserModel(userName, self.serialize())
        
        print('Finished training')
        
        return True
        
    def serialize(self):
        pickle_string = str(base64.b64encode(pickle.dumps(self.regr, protocol=2)))
        pickle_string = pickle_string[1:]
        return pickle_string
