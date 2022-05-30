# -*- coding: utf-8 -*-
"""nearest_lat_lon.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10nrn-nDJlgfi1zjP7nqtJ8WN44CRF51w
"""

from google.colab import drive 
drive.mount('/content/drive')

import pandas as pd
import numpy as np

data=pd.read_csv('/content/drive/MyDrive/out.csv')

data.head()

data.columns =['CC', 'address1', 'address2','unused','unused2','latitude','longitude'] 
data.drop('unused',axis=1,inplace=True)  
data.drop('unused2',axis=1,inplace=True)

userlat=float(input("Enter the latitude: "))

userlon=float(input("Enter the longitude: "))

from math import radians, cos, sin, asin, sqrt


from math import radians, cos, sin, asin, sqrt 
def haversine(lon1, lat1, lon2, lat2):
  
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
  
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
  
    km = 6371* c
    return km

data['distance'] = [haversine(data.longitude[i],data.latitude[i],userlon,userlat) for i in range(len(data))]
data['distance'] = data['distance'].round(decimals=3)

data.head()

val=min(data['distance'])

print("NEAREST LOCATION to",userlat ,"latitude and ",userlon,"longitude is/are :- \n") 
print(data.loc[data['distance'] == val])
