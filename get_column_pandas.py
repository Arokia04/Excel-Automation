import pandas
data = pandas.read_csv('sample.csv')
column2 = data.iloc[:,4:]
print(column2)
