import pandas as pd
import numpy as np
def pout(c1,c2,c3,c4,c5,c6,c7,c8):
    out = rg.predict(np.array([float(c1),float(c2),float(c3),float(c4),float(c5),float(c6),float(c7),float(c8)]).reshape(1,-1))
    return int(out[0])

data = pd.read_csv("C:\Users\skeer\OneDrive\Desktop\react-django\backend\heart_failure_clinical_records_dataset.csv")


x = data.iloc[:,:-1]
y = data.iloc[:,-1]
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size = 0.2,random_state = 1,shuffle = True)

from sklearn.linear_model import LogisticRegression
rg = LogisticRegression()
rg.fit(xtrain,ytrain)