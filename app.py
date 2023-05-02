import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
import pandas_datareader as data
from sklearn.preprocessing import MinMaxScaler
import streamlit as slt
plt.style.use('fivethirtyeight')

slt.title('Stock Price Prediction')

# user_input = slt.text_input('Enter Stock Ticker', 'RELIANCE.NS.csv')

stocks = ('SBIN.NS.csv','TCS.csv','TATAMOTORS.NS.csv','ADANIPORTS.NS.csv','RELIANCE.NS.csv','M&M.NS.csv','HEROMOTOCO.NS.csv','BHARTIARTL.NS.csv')

user_input = slt.selectbox('Select Dataset For Prediction',stocks)

df = pd.read_csv(user_input)
df= df.dropna()


slt.subheader('Data from 2012 - 2022')
slt.write(df.head(7))

slt.subheader('Description of the Stock',user_input)
slt.write(df.describe())


# Plottning the Closing Price
slt.subheader('Closing Price vs Time')
fig = plt.figure(figsize=(12, 6))
plt.plot(df.Close)
slt.pyplot(fig)


# Extracting the Close column
data = pd.DataFrame(df['Close'])
data_set = data.values


# Scalling using MinMax Scaler
scaler = MinMaxScaler(feature_range=(0, 1))
scaleddata = scaler.fit_transform(data_set)

train_size = int(len(data_set) * 0.80)

# Training Dataset
train_data = scaleddata[:train_size, :]


# Load the Model
model = load_model('our_model.h5')


# Test Data
test_data = scaleddata[train_size-100:, :]
x_test = []                        
y_test = data_set[train_size:, :]

for i in range(100, len(test_data)):
    x_test.append(test_data[i-100:i, 0])


# Scalling of test data
x_test = np.array(x_test)

# Prediction 
pred = model.predict(x_test)
pred = scaler.inverse_transform(pred)



# Plotting of the Predicted Values
train = data[:int(len(train_data))]
valid = data[int(len(train_data)):]

valid['Prediction'] = pred


slt.subheader('Prediction vs Original')
fig2 = plt.figure(figsize=(10, 5))
plt.title('Model')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.plot(train['Close'])
plt.plot(valid[['Close', 'Prediction']])
plt.legend(['Train', 'Validation', 'Prediction'], loc='upper left')
slt.pyplot(fig2)


# Accuracy and Scores
slt.subheader('Accuracy and Other Scores')
rmse = np.sqrt(np.mean(pred-y_test)**2)
slt.write('RMSE Value: ',rmse)
errors = abs(pred - y_test)
mape = 100 * (errors / y_test)
accuracy = 100 - np.mean(mape)
slt.write('Accuracy: ',accuracy)  

# Comparision
slt.subheader('Comparison Between Actual Close Price and Predicted Price')
slt.write(valid)


