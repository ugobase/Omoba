#!/usr/bin/env python
# coding: utf-8

# In[268]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv


# In[269]:


#Read the file, made the fisrt row the columns/header
#Made the other rows as the rows, created an empty list and appended the new rows and columns
with open("Population.csv", "r") as file:
    parser = csv.reader(file)
    columns = next(parser)
    rows = [row for row in parser]
data = []
for rows in rows:
    data.append(dict(zip(columns, rows)))


# In[270]:


#Created a dataframe for the new file
data_set = pd.DataFrame(data)


# In[271]:


#Viewed the file created
data_set


# In[272]:


data_set.info()


# In[273]:


data_set.info()


# In[274]:


#Top 5 largest of the data
data_set.head()


# In[275]:


#Last 5 rows of the data
data_set.tail()


# In[276]:


with open("cities_emissions_new.csv", "r") as file:
    parser = csv.reader(file)
    columns = next(parser)
    rows = [row for row in parser]
dataset = []
for rows in rows:
    dataset.append(dict(zip(columns, rows)))


# In[277]:


dataset = pd.DataFrame(dataset)
dataset


# In[278]:


dataset.info()


# In[279]:


merged_dataset = pd.merge(data_set, dataset, on=['org_id', 'crm_org_name', 'crm_country_name'])


# In[280]:


#merged_dataset.to_csv('merged_dataset.csv', index=False)


# In[281]:


merged_dataset


# In[282]:


merged_dataset['Population'] = pd.to_numeric(merged_dataset['Population'])
merged_dataset['Polulation per km2'] = pd.to_numeric(merged_dataset['Polulation per km2'])
merged_dataset['land area km2'] = pd.to_numeric(merged_dataset['land area km2'])
merged_dataset['org_id'] = merged_dataset['org_id'].astype(int)
merged_dataset['direct_emissions_metric_tonnes_co2e'] = pd.to_numeric(merged_dataset['direct_emissions_metric_tonnes_co2e'])


# In[283]:


merged_dataset.info()


# In[284]:


merged_dataset.isna().sum()


# In[285]:


merged_dataset = merged_dataset.dropna()


# In[286]:


merged_dataset.isna().sum()


# In[287]:


merged_dataset.info()


# In[288]:


merged_dataset['row_name'].unique()


# In[289]:


merged_dataset['row_name'] = merged_dataset['row_name'].replace([''], 'Total Emissions (excluding generation of grid-supplied energy)')


# In[290]:


merged_dataset.shape


# In[291]:


merged_dataset.dtypes


# In[292]:


merged_dataset


# In[293]:


#Top 5 largest values in the 'value' column
merged_dataset.nlargest(5, 'Population')


# In[294]:


#Top 5 least values in the 'value' column
merged_dataset.nsmallest(5, 'Population')


# In[295]:


merged_dataset[merged_dataset['crm_country_name'].isin(['United States of America', 'Brazil', 'Nigeria'])].shape[0]


# In[296]:


merged_dataset[merged_dataset['crm_org_name'].str.contains('City of West Hollywood')].shape[0]


# In[297]:


merged_dataset[merged_dataset['crm_org_name'].str.contains('City of Lagos')].shape[0]


# In[298]:


merged_dataset[merged_dataset['crm_org_name'].isin(['City of West Hollywood', 'Ville de Monaco', 'City of Lagos'])].shape[0]


# In[299]:


merged_dataset[merged_dataset['crm_country_name'].isin(['Nigeria'])]


# In[300]:


corre=merged_dataset[['Population' , 'land area km2', 'direct_emissions_metric_tonnes_co2e']].corr()
corre


# In[301]:


plt.figure(figsize = (10,5))
sns.heatmap(corre.corr(), annot = True, fmt = '0.1f')


# In[302]:


details_country = merged_dataset.groupby('crm_country_name', as_index =False)[
    'direct_emissions_metric_tonnes_co2e',
    'Population',
    'land area km2'
].sum().sort_values(by='direct_emissions_metric_tonnes_co2e', ascending=False)

details_country.head()


# In[313]:


details_country["crm_country_name"].nunique()


# In[303]:


plt.figure(figsize=(20,8))
sns.barplot(data= details_country, x='crm_country_name', y='direct_emissions_metric_tonnes_co2e')
plt.xticks(rotation=90)
plt.show()


# In[304]:


plt.figure(figsize=(25,8))
sns.barplot(data= details_country, x='crm_country_name', y='Population')
plt.xticks(rotation=90)
plt.show()


# In[311]:


plt.figure(figsize=(15,8))
sns.scatterplot(data=merged_dataset, x="crm_country_name", y="Population", hue ="row_name" )
plt.xticks(rotation=90)
plt.show()


# In[322]:


plt.figure(figsize=(15,8))
sns.scatterplot(data=details_country, x="crm_country_name", y="Population", hue = "Population" )
plt.xticks(rotation=90)
plt.show()


# In[331]:


plt.figure(figsize=(15,8))
sns.scatterplot(data=details_country, x="crm_country_name", y="direct_emissions_metric_tonnes_co2e", hue = "Population" )
plt.xticks(rotation=90)
plt.show()


# In[306]:


plt.figure(figsize=(16,8))
sns.boxplot(data = merged_dataset, x = 'crm_country_name', y = 'Population')
plt.xticks(rotation=90)
plt.show()


# In[353]:


plt.figure(figsize=(25,8))
sns.displot(data=details_country["Population"], kde = True)
#plt.xticks(rotation=90)
#plt.show()


# In[352]:


plt.figure(figsize=(15,8))
sns.displot(data=details_country["direct_emissions_metric_tonnes_co2e"], kde = True)


# In[ ]:




