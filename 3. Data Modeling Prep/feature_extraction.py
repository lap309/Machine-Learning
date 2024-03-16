## MUST BE SCALED BEFORE CONDUCTIN FEATURE EXTRACTION
### Combining existing features to produce more useful results



#### Dimensionality Reduction with PCA

#running PCA and deciding which number of components will add up to a sufficiently large proportion of the variance (typical goal 95%)
# conduct PCA without all features to compute the minimum number of dimensions required to preserve 95% of the variance
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

