#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 18:08:14 2024

@author: eren
"""


"""
Veri Seti Hakkında
Valorant, beş oyuncudan oluşan iki takımın bir oyunda 13 raundu 
ilk kazanan olmak için yarıştığı rekabetçi bir çok oyunculu 
birinci şahıs nişancı (FPS) oyunudur. “Dereceli” oyun modu, 
en rekabetçi oyuncuların mümkün olan en yüksek dereceyi elde 
etmek için oynadıkları yerdir. Valorant dereceli oyununda 
9 bölüm vardır. Oyuncu becerilerinin artan sırasına göre 
bunlar: Iron, Bronze, Silver, Gold, Platinum, Diamond, 
Ascendant, Immortal ve Radiant. Bu veri kümesi, Bir valorant
oyuncusunun dereceli yolculuğunun ilk 1000 oyunudur.
"""




#Importing Necessary Librabries for Data Preprocessing & Visualization
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



df=pd.read_csv('/mnt/c/Users/CASPER/OneDrive/Masaüstü/Valorant Veri Seti/valorant_games.csv')


print(df.head()) #Check the Data

print(df.describe()) #Understand Data

print(df.info()) #Understand Data Type & Values

print(df.isnull().sum()) #Check Null Values

print(df.columns) #Check All Columns


#Identify Win-Lose Rate
plt.figure(figsize=(8,3))
sns.countplot(data=df,x='outcome',hue='outcome',palette='rocket')
plt.xlabel('Outcomes')
plt.ylabel('Count')
plt.title('Outcome Analysis')
plt.show()


#Identify most used agents
plt.figure(figsize=(8,4))
sns.countplot(data=df,x='agent',hue='agent',order=df['agent'].value_counts().index,palette='deep')
plt.xlabel('Agent Frequency')
plt.ylabel('Count')
plt.title('Agent Frequency')
plt.show()


#Identify Most Played Map
plt.figure(figsize=(8,4))
sns.countplot(data=df,y='map',hue='map',order=df['map'].value_counts().index,palette='deep')
plt.xlabel('Map Frequency')
plt.ylabel('Count')
plt.title('Map Frequency')
plt.show()



#Agent Outcome Analysis
plt.figure(figsize=(8,4))
sns.countplot(data=df,x='agent',hue='outcome',order=df['agent'].value_counts().index,palette='rocket')
plt.xlabel('Outcomes')
plt.ylabel('Count')
plt.title('Outcome Analysis - Agentwise')
plt.show()


#Map outcome Analysis
plt.figure(figsize=(8,4))
sns.countplot(data=df,x='map',hue='outcome',order=df['map'].value_counts().index,palette='rocket')
plt.xlabel('Outcomes')
plt.ylabel('Count')
plt.title('Outcome Analysis - Map')
plt.show()



#Grouby Data For Agent
data_a=df.groupby(['agent'])[['kills','deaths','assists']].sum()
data_a=data_a.reset_index()
data_a = data_a.sort_values(by='kills', ascending=False)
print(data_a)


#Agentwise Performace
plt.figure(figsize=(8, 6))
sns.barplot(x='agent', y='kills', data=data_a,hue='agent',palette='viridis')
sns.lineplot(x='agent', y='deaths', data=data_a,color='red',marker='o',label='Deaths',linewidth='2')
sns.lineplot(x='agent', y='assists', data=data_a,marker='s',color='blue',label='Assists',linewidth='2')
plt.xlabel('Agent')
plt.ylabel('Total Kills')
plt.title('Agent Performance')
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for readability
plt.tight_layout()
plt.show()



#Groupby Data Mapwise
data_b=df.groupby(['map'])[['kills','deaths','assists']].sum()
data_b=data_b.reset_index()
data_b = data_b.sort_values(by='kills', ascending=False)
print(data_b)


#Mapwise Performace
plt.figure(figsize=(8, 6))
sns.barplot(x='map', y='kills', data=data_b,hue='map',palette='viridis')
sns.lineplot(x='map', y='deaths', data=data_b,color='red',marker='o',label='Deaths',linewidth='2')
sns.lineplot(x='map', y='assists', data=data_b,marker='s',color='blue',label='Assists',linewidth='2')
plt.xlabel('Map')
plt.ylabel('Total Kills')
plt.title('Map Performance')
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for readability
plt.tight_layout()
plt.show()


#Identify Ranks
print(df['rank'].unique())
print(df['rank'].value_counts())


#Grouby Data Rankwise
data_c=df.groupby(['rank'])[['kills','deaths','assists']].sum()
data_c=data_c.reset_index()
data_c = data_c.sort_values(by='kills', ascending=False)
print(data_c)


#Rankwise Perforamance
plt.figure(figsize=(8,4))
sns.barplot(data=data_c,x='rank',y='kills',hue='rank',palette='viridis')
sns.lineplot(x='rank', y='deaths', data=data_c,color='red',marker='o',label='Deaths',linewidth='2')
sns.lineplot(x='rank', y='assists', data=data_c,marker='s',color='blue',label='Assists',linewidth='2')
plt.xlabel('Rank')
plt.ylabel('Total Kills')
plt.title('Rank Performance')
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for readability
plt.tight_layout()
plt.show()



#Convert date column to Datetime
df['date'] = pd.to_datetime(df['date'])


plt.figure(figsize=(8,4))
sns.lineplot(data=df,x='date',y='rank',color='red',linewidth='2')
plt.xlabel('Date')
plt.ylabel('Rank')
plt.title('Rank Progression')
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for readability
plt.tight_layout()
plt.show()



# Korelasyon Matrisini Çizdirme
plt.figure(figsize=(12,8))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(),annot=True,cmap='rocket')
plt.title('Correlation Heatmap')
plt.show()


#Data Reference
print(df.head())

