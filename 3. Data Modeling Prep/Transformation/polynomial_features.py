from sklearn.preprocessing import PolynomialFeatures


poly_feat = PolynomialFeatures(degree = 2)  #will output the interaction terms of each one of our X data as well as all the different features squared
poly_feat = poly_feat.fit(x_data)
x_poly = poly_feat.transform(x_data)
