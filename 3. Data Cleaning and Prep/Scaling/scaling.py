############# Normalization
# there are several pre-built normilization programs\packages
#Min-Max Scaler (General normalization): Subtract mean, divide by standard deviation. from sklearn package which scales each feature between zero and one

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()                             # Set up scaler model

# Alternative is zero mean, unit variance
# from sklearn.preprocessing import StandardScaler

scaler.fit(x_train)                                 # apply\fit the scaler on the training dataset
x_train = scaler.transform(x_train)                 # scale the training set

x_test = scaler.transform(x_test)                   # scale the test set
