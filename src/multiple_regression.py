import pandas as pd
from sklearn import linear_model
import numpy as np

class MultipleRegression: 
    def run(self):
        data = {'top': [1, 3, 4, 5],
                'bottom': [3, 1, 4, 5],
                'right': [7, 2, 4, 7],
                'left': [4, 6, 1, 4],
                'center': [2, 2, 4, 5],
                'lose': [1, 1, 1, 2],   
                }

        df = pd.DataFrame(data)

        x = df[['top','bottom', 'right', 'left', 'center']]
        y = df['lose']
        
        # with sklearn
        regr = linear_model.LinearRegression()
        regr.fit(x.values, y)

        print('Intercept: \n', regr.intercept_)
        print('Coefficients: \n', regr.coef_)

        print(regr.predict(np.array([[3, 5, 2, 1, 3]])))
        print(regr.predict(np.array([[1, 2, 1, 0, 4]])))
