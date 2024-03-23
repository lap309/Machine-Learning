## MUST BE SCALED BEFORE CONDUCTIN FEATURE EXTRACTION
### Combining existing features to produce more useful results



#### Dimensionality Reduction with PCA
# helpful for unsupervised learning. Reducing the number of dimensions can simplify modelling and allow classifications to be performed
####### Principle Component Analysis (PCA) method:
## does rotations of data in a 2D array to decompose the array into combination vectors that are orthogonal and can be ordered according to the amount of info they carry
#running PCA and deciding which number of components will add up to a sufficiently large proportion of the variance (typical goal 95%)
# conduct PCA without all features to compute the minimum number of dimensions required to preserve 95% of the variance

#Version 1
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
####################################################################################################################################
#Version 2

pca_dim = PCA()
pca_dim.fit(x_train)
cumsum = np.cumsum(pca_dim.explained_variance_ratio_)
d = np.argmax(cumsum>=0.95)+1
print(d)

px.area( x=range(1, cumsum.shape[0] +1),
       y=cumsum,
       labels = {'x':'# components','y': 'Explained Variance'})

# Alternative, just set the n_components to reach
pca = PCA(n_components= 0.95)     # creating the pca element
pca.fit_transform(x_train)    #applying pca to our data

exp_var = pca.explained_variance_ratio_       #explained variance ratio indicates the porportion of the original data aligns with the PCA we just 
                                              #created. We want this to be as high as possible within reason
print(exp_var)

with plt.style.context('dark_background'):
  plt.figure(figsize=(6,4))

plt.bar(range(7), exp_var, alpha= 0.5, align = 'center', label = 'individual explaine variance')
plt.ylabel('Explained Variance Ratio')
plt.xlabel('Principal Components')
plt.legend(loc= 'best')
plt.tight_layout()

