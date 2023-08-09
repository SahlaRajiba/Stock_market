import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout, GRU, Bidirectional
from keras.optimizers import SGD
import math
from sklearn.metrics import mean_squared_error

def gru_aave():
    def plot_predictions(test,predicted):
        print("=================================")
        print(predicted)
        # plt.plot(test, color='red',label='visiting records')
        plt.plot(predicted, color='blue',label='2 Year IBM Stock Data.csv')
        plt.title('visiting records')
        plt.xlabel('Time')
        plt.ylabel('visiting count')
        plt.legend()
        plt.show()

    def return_rmse(test,predicted):
        rmse = math.sqrt(mean_squared_error(test, predicted))
        print("The root mean squared error is {}.".format(rmse))

    # First, we get the data
    dataset = pd.read_csv(r'E:\django\stockmarket\static\ibm.csv', index_col='date', parse_dates=['date'])
    print(dataset.head())

    training_set = dataset[:'2020'].iloc[:,3:4].values
    test_set = dataset['2021':].iloc[:,3:4].values

    print("================training_set,test_set")
    print(training_set[0])
    print(test_set[0])
    print("================training_set,test_set")
    print(type(training_set[0]))
    print(type(test_set[0]))

    # dataset["Marketcap"][:'2020'].plot(figsize=(16,4),legend=True)
    # dataset["Marketcap"]['2020':].plot(figsize=(16,4),legend=True)
    # plt.legend(['Training set (Before 2017)','Test set (2017 and beyond)'])
    # plt.title('visiting records')
    # plt.show()

    # Scaling the training set
    sc = MinMaxScaler(feature_range=(0,1))
    training_set_scaled = sc.fit_transform(training_set)

    X_train = []
    y_train = []
    print(len(training_set_scaled))
    for i in range(60,len(training_set_scaled)):
        X_train.append(training_set_scaled[i-60:i,0])
        y_train.append(training_set_scaled[i,0])
    X_train, y_train = np.array(X_train), np.array(y_train)


    # Reshaping X_train for efficient modelling
    X_train = np.reshape(X_train, (X_train.shape[0],X_train.shape[1],1))
    print(dataset)

    dataset_total = pd.concat((dataset["close"][:'2020'],dataset["close"]['2021':]),axis=0)
    inputs = dataset_total[len(dataset_total)-len(test_set) - 60:].values
    inputs = inputs.reshape(-1,1)
    inputs  = sc.transform(inputs)

    print(X_train.shape,"input shape=================")




    print("============================Xtrain,y_train")
    print(X_train[0] )
    print(y_train[0])
    print("============================")
    print(type(X_train) )
    print(type(y_train))
    print("============================")
    X_test = []
    print(len(inputs))
    for i in range(60,len(inputs)):
        X_test.append(inputs[i-60:i,0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0],X_test.shape[1],1))

    # print("============================GRU_visiting records")
    # print(GRU_predicted_stock_price[0])
    # print(type(GRU_predicted_stock_price[0]) )
    # print("============================GRU_visiting records")
    # GRU_predicted_stock_price = sc.inverse_transform(GRU_predicted_stock_price)
    # print(GRU_predicted_stock_price[0])
    # print(type(GRU_predicted_stock_price[0]) )
    # print("============================")
    # print(GRU_predicted_stock_price)
    # return GRU_predicted_stock_price
    # Visualizing the results for GRU
    # plot_predictions(test_set,GRU_predicted_stock_price)
gru_aave()
