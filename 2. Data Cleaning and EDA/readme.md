# EDA Libraries
- matplotlib: main library with a lot of flexibility but everything has to be set up manually
- pandas : is a convenient wrapper function around the matplotlib library. Less manual but less flexible and less powerful compared to working with the original version of matplotlib
- seaborn : pretty  matplotlib<br>
            has certain specialty plots like linear model plots, pairwise correlation plots and many others, which would otherwise take a long time using just matplotlib
            once imported Seaboard preferences are Incorporated by matplotlib. So if you import Seaborn and then go back to using matplotlib, it would look like you're still within the visualization format that Seaborn has


So this will determine if the data that we're looking at actually makes sense, or if we need further cleaning, or if more data is actually needed. EDA will help us identify patterns and trends in the actual data set. <br> <br>

Summary Statistics: Mean, Median, Average, Min, Max, Correlations <br>
Shape/Distributions :Histograms, Scatter, Box Plots, etc <br>
Corerlations: Scatter Plot



| Graph                  | Type of Data             | What to look for/When to use |
| -----------------------| ------------------------ | -----------------------|
| Bar Chart              | Categorical Data         | Count/Frequncy distribution of each category  |
| Comparative Bar Charts | Categorial Data          | Categorical data for groups |
| Stacked Bar Char       | Categorical Data         | Proportions of categories |
| Pie Chart              | Categorical data with a small number of possible categories | The proportions of each category in the dataset|
| Dot Plots              | Small numerical datasets | - A representative or typical value in the dataset  |
|                        |                          | - The extent to which the data values are spread out  |
|                        |                          | - The nature of the distribution of values along the number line   |
|                        |                          | - The presence of unusual values in the data set |
|                        |                          | - Locating groupings in the data, univariate, bivariate, multivariate data |
| Histogram              | Numerical Data (continuous and discrete) | - General distribution, shape and extent of spread or variability |
|                        |                          | - Center or typical value. Location and number of peaks |
|                        |                          | - Presence of gaps and outliers|
| Cumulative Relative Frequency |    | |
| Scatter Plot           | Bivariate Numerical Data  (x and y)| correlations or the relationship between two different columns |
|                        |                          | Shape, Relation, Trend |
| Box Plot               | Numerical Data           | Distribution, Outliers
| Line Plots             | Numerical                | 
| Time Series            | Date Time                | Change over time|

# Data Cleaning
## Missing Data/NULL Values

__Remove Duplicates:__ <br>
Pro: Easy and quick process. This is good for samples with a very small proportion of missing data <br>
Con: Could be detrimental if empty rows actually mean something. ex: call time of NA means a hang up at a telemarketer center <br>
So in this case, just deleting the null values would be deleting a whole category of outcomes and thus creating biased data <br><br>

__Masking/Assigning Categories:__ <br>
Creating a category for missing values. This assumes that the missing values actually mean something <Br>
Pro: You don't lose any data <br>
Con: The assumption that the missing values have meaning adds a level of uncertainty to data. Can we really be sure that all the cases of null values mean the same thing? <br><br>

__Impute data:__ <br>
Replace null values with substituted values (mean, median, mode)<br>
Pro: You don't lose any data <br>
Con: The calculated values that will replace the null values will never be truly accurate. And it is impossible to know how close or how far off from the real values our imputed values will be.

## Identifying Outliers

__Plots__
- Histogram
- Density Plot
- Box Plot

__Statistics__
- IQ Range Box Plot
- Standard Deviation

__Residuals__
-Checking Residuals

## Handling outliers
__Removing Outliers__
Pro: no more outliers <br>
Con: may have lost an important value, or observation that might be helpful to the model

__Assign a new value to the outlier__
Pro: no more outliers, and you can keep all the original observations <br>
Con: You are still losing the original value of the data point

__Transform__
ex: Log transformations

__Imputation__
Ex: Regression
Pro: no more outliers, may be a more accurate value, and keep all the original observations <br>
Con: Requires a lot more work than the other options, 

__Residuals__ (assumes you already have a model) <br>
The difference betwen the actual and predicted values of the outcome variable <br>
- Standardized- residuals divided by the standard error
- Deleted- remove the outlier from the dataframe, then re-run the new model and see if there's a big difference between the original model and the model with the deleted observation
- Studentized- take the deleted residuals, rerun the model, then take the standardization of that rerun, and apply it to the original observation

## Encoding / Dummy Variable Creation
Applied to categorical features to give them numeric values <br>
The two types: <Br>
Nominal: categorical variables with NO order ex: [true, false], [red, green, blue]  <br>
Ordinal: categorical variables with an order ex: [high, medium, low], [cold, warm, hot] <Br>
<Br>
Types of Encoding: <br>
* Binary  Encoding- converts variables to 0 or 1
* Hot One Encoding - creates a new column for each value in the original column
* Ordinal Encoding - converting values in the column into an ordered number set ( ex: low = 1, medium = 2, high = 3)
