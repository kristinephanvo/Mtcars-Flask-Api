import pandas as pd
import numpy as np
from  sklearn.linear_model import LinearRegression

data = pd.read_csv("mtcars.csv")

labels = data['mpg']

train1 = data.drop(['mpg', 'model'],axis=1)

col_imp = ["cyl","disp", "hp", "drat", "wt", 
           "qsec", "vs", "am", "gear", "carb"]

clf = LinearRegression()
clf.fit(train1[col_imp], labels)

def predict(dict_values, col_imp=col_imp, clf=clf):
    x = np.array([float(dict_values[col]) for col in col_imp])
    x = x.reshape(1,-1)
    y_pred = clf.predict(x)[0]
    return y_pred
