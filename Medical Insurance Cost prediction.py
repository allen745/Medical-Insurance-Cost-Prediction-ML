# data --> data analysis--> data preprocessing --> train test split --> Linear Regression Trained linear regression new data --> prediction

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

# data collection and analysis
# loading data from csv to file to pandas dats frame

insurance_data = pd.read_csv(r'C:\Users\allen\OneDrive\Desktop\understanding\data\insurance.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print(insurance_data.head())

# number of rows and columns
print(insurance_data.shape)

# getting some information about data set
print(insurance_data.info())

# checking nul values
print(insurance_data.isnull().sum())

# data analysis
print(insurance_data.describe())

# distribution of age values
sns.set()
plt.figure(figsize=(6,6))
sns.displot(insurance_data['age'])
plt.title('Age Distribution')
plt.show()

# gender column
plt.figure(figsize=(6,6))
sns.countplot(x = 'sex', data=insurance_data)
plt.title('Sex Distribution')
plt.show()
print(insurance_data['sex'].value_counts())

# bim distribution
plt.figure(figsize=(6,6))
sns.displot(insurance_data['bmi'])
plt.title('BMI Distribution')
plt.show()

# children column
plt.figure(figsize=(6,6))
sns.countplot(x = 'children', data=insurance_data)
plt.title('Children')
plt.show()

# smoker column
plt.figure(figsize=(6,6))
sns.countplot(x='smoker', data=insurance_data)
plt.title('smoker')
plt.show()

# region column
plt.figure(figsize=(6,6))
sns.countplot(x='region', data=insurance_data)
plt.title('region')
plt.show()

# distribution of charges value
plt.figure(figsize=(6,6))
sns.displot(insurance_data['charges'])
plt.title('Charges Distribution')
plt.show()

# encoding the categorial features
insurance_data.replace({'sex':{'male':0, 'female':1}}, inplace=True)

# encoding smoker
insurance_data.replace({'smoker':{'yes':0, 'no':1}}, inplace=True)

# encoding region
insurance_data.replace({'region':{'southeast':0, 'southwest':1, 'northeast':2, 'northwest':3}}, inplace=True)

# splitting features and target

x = insurance_data.drop(columns='charges')
y = insurance_data['charges']

# splitting into test data and train data

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 2)

# modal training
# Linear regression

regressorv = LinearRegression()
regressorv.fit(x_train, y_train)

# modal evalution

training_data_prediction = regressorv.predict(x_train)
r2_train = metrics.r2_score(y_train, training_data_prediction)
print("R squared of training data is ",r2_train)

test_data_prediction = regressorv.predict(x_test)
r2_test = metrics.r2_score(y_test, test_data_prediction)
print("R squared of testing data is ",r2_test)


# building predictive system

input_data = (31,1,25.74,0,1,0)

# changing input data to numpy array

input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = regressorv.predict(input_data_reshaped)

print("THE INSURANCE COST IN USD ", prediction[0])


