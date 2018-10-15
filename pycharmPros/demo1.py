import pandas as pd
print(pd.__version__)
print(pd.Series(['San Francisco', 'San Jose', 'Sacramento']))
city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])
print(pd.DataFrame({ 'City name': city_names, 'Population': population }))
california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")
print(california_housing_dataframe.describe())
print(california_housing_dataframe.hist('housing_median_age'))
