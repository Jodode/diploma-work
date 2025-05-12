import pandas as pd

data = pd.read_csv('data.csv')

data['issue_d'] = pd.to_datetime(data['issue_d'], format='%b-%Y')
data = data[(data['issue_d'] >= '2016-01-01') & (data['issue_d'] < '2018-01-01')].sort_values(by=['issue_d', ])
data = data[data['application_type'] == 'Individual']
data.to_parquet('loans_individual_data.parquet')