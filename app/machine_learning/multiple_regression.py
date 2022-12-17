import pandas as pd
from sklearn import linear_model
import numpy as np
from app.database.database_connection import DatabaseConnection
import pickle
import base64

class MultipleRegression: 
    def __init__(self, userName):
        self.regr = None    
        self.featureList = []
        self.userName = userName

    def trainModelForUser(self):
        
        print('Train model for ' + self.userName)
        databaseConnection = DatabaseConnection()
        
        runs = databaseConnection.getAllRunsByUser(self.userName)
        
        data = {
            'top_field': [],
            'bottom_field': [],
            'right_field': [],
            'left_field': [],
            'center_field': [],
            'lose_count': []
        }
        
        for run in runs:
            runString = list(map(str, run))
            data['top_field'].append(runString[0])
            data['bottom_field'].append(runString[1])
            data['right_field'].append(runString[2])
            data['left_field'].append(runString[3])
            data['center_field'].append(runString[4])
            data['lose_count'].append(runString[5])

        if (len(data['top_field']) == 0):
            return False

        df = pd.DataFrame(data)

        x = df[['top_field','bottom_field', 'right_field', 'left_field', 'center_field']]
        x = pd.get_dummies(data=x)
        
        print(x.columns);
        
        self.featureList = x.columns;
        
        y = df['lose_count']
        
        # with sklearn
        regr = linear_model.LinearRegression()
        regr.fit(x.values, y.values)

        print('Intercept: \n', regr.intercept_)
        print('Coefficients: \n', regr.coef_)
        
        self.regr = regr
        
        # print(pd.DataFrame(regr.coef_,x.columns,columns=['Coefficient']));
        
        databaseConnection.updateUserModel(self.userName, self.serialize(self.regr), self.serialize(self.featureList))
        
        return True
        
    def serialize(self, target):
        pickle_string = str(base64.b64encode(pickle.dumps(target, protocol=2)))
        pickle_string = pickle_string[1:]
        return pickle_string

    def getModel(self):
        databaseConnection = DatabaseConnection()
        user = databaseConnection.getUserByName(self.userName)
        if (user and user[2] and len(user[2]) > 1):
            self.regr = pickle.loads(base64.b64decode(user[2]))
            self.featureList = pickle.loads(base64.b64decode(user[3]))

    def predict(self, top_field, bottom_field, right_field, left_field, center_field):
        if (self.regr != None):
            
            failFields = []
            failFields.append('top_field_' + str(top_field))
            failFields.append('bottom_field_' + str(bottom_field))
            failFields.append('right_field_' + str(right_field))
            failFields.append('left_field_' + str(left_field))
            failFields.append('center_field_' + str(center_field))
            
            predictArray = [];
            for feature in self.featureList:
                value = 0
                for fails in failFields:
                    if (fails == feature):
                        value = 1
                predictArray.append(value)
            
            value = self.regr.predict(np.array([predictArray]))[0]
            print(value)
            print([top_field, bottom_field, left_field, center_field, right_field])
            return value