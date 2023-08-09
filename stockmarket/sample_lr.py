import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from warnings import simplefilter
from sklearn.linear_model import LinearRegression

# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd


dataset = pd.read_csv(r'E:\django\stockmarket\static\ibm.csv', index_col='date', parse_dates=['date'])
#print(dataset.head())

training_set = dataset[:'2020'].iloc[:, 3:4].values
test_set = dataset['2021':].iloc[:, 3:4].values

#print("================training_set,test_set")
#print(training_set[0])
#print(test_set[0])
#print("================training_set,test_set")
#print(type(training_set[0]))
#print(type(test_set[0]))



X_train = []
y_train = []
#print(len(training_set))
for i in range(60, len(training_set)):
    r=training_set[i - 60:i, 0]
    row=[]
    for ii in r:
        row.append(ii)
    X_train.append(row)
    y_train.append(training_set[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)

# Reshaping X_train for efficient modelling
# X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
#print(dataset)

dataset_total = pd.concat((dataset["close"][:'2020'], dataset["close"]['2021':]), axis=0)
inputs = dataset_total[len(dataset_total) - len(test_set) - 60:].values
inputs = inputs.reshape(-1, 1)


#print("============================Xtrain,y_train")
#print(X_train[0])
#print(y_train[0])
#print("============================")
#print(type(X_train))
#print(type(y_train))
#print("============================")
X_test = []
#print(len(inputs))
for i in range(60, len(inputs)):
    r = training_set[i - 60:i, 0]
    row = []
    for ii in r:
        row.append(ii)
    X_test.append(row)
X_test = np.array(X_test)
# X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))




# print(len(X_train[0]))
# print(len(X_train[0][0]))
# Train the model
print(X_train[0])
model = LinearRegression()
model.fit(X_train, y_train)

# Store the fitted values as a time series with the same time index as
# the training data
y_pred =model.predict(X_test)
# y_pred = pd.Series(model.predict(X), index=X.index)

print("==========================================================")
print("==========================================================")
print("==========================================================")
print("==========================================================")
print("==========================================================")
print(y_pred)

for i in range(0, len(y_pred)):
    print(y_pred[i], "+++++++++++++++++++++++===============*******************")
    print(y_train[i])
    diff = y_pred[i] - y_train[i]
    print(diff, "&&&&&&&&&&&")

# print(len(X_test))
# print(len(y_pred))