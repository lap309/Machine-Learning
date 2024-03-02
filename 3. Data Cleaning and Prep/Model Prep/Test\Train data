############# Prepping Test and Data Sets
from sklearn.model_selection import train_test_split

x = df[input_features]
y = df[outcome]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.7, random_state = 42)    #will put 70% of data into the training set, 30% to test
                                                                                                  # 70/30 train & test is normal
                                                                              # random_state specifies the random number generator, allowing for reproduceability
                                                                              # this will make the random number generator produce the same "Random" split in the future
#############Checking for missing data
# We will use the training median to replace missing values in both the test and training data, this will avoid data leaking between the two sets. Usually we are not missing data at random

# impute missing values from the training set
x_train = x_train.fillna(x_train.median())
x_test = x_test.fillna(x_train.median())

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

################################# Dimensionality Reduction
# helpful for unsupervised learning. Reducing the number of dimensions can simplify modelling and allow classifications to be performed
####### Principle Component Analysis (PCA) method:
## does rotations of data in a 2D array to decompose the array into combination vectors that are orthogonal and can be ordered according to the amount of info they carry

from sklearn import decomposition
import matplotlib.pyplot as plt
import numpy as np

pca = decomposition.PCA(n_components = 2)
pca.fit(x)
x_pca = pca.transform(x)

fig = plt.figure(1, figsize=(4,4))
plt.clf()
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap=plt.cm.nipy_spectral, 
        edgecolor='k',label=y)
plt.colorbar(boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.savefig("pca.svg")

############ t-distributed Stochastic Neighbor Embedding (t-SNE)

from sklearn import manifold
import matplotlib.pyplot as plt
import numpy as np

tsne = manifold.TSNE(n_components=2, init='pca',
        random_state = 0)
X_tsne = tsne.fit_transform(X)
fig = plt.figure(1, figsize=(4, 4))
plt.clf()
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap=plt.cm.nipy_spectral,
        edgecolor='k',label=y)
plt.colorbar(boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.savefig("tsne.svg")
