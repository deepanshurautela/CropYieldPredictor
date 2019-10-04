import pandas as pd
import numpy as np

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

data_input = pd.read_excel('Data.xlsx')
y = data_input['Crop']
x = data_input.drop(['Crop'],axis=1)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.1)

model = GaussianNB()	#create a gaussian classifier
model.fit(x,y)	#train the model using training sets

def search_crop(input_data):
	test_data = np.array([[input_data[value] for value in input_data]])
	predicted = model.predict(test_data)
	return predicted[0]