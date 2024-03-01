# Missing Data

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
