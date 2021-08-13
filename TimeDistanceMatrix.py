#!/usr/bin/env python
# coding: utf-8

# ### 1) Cálculo das Matrizes de Tempo e Distância

# > o presente código utilizou como base Projeto OSRM (https://github.com/Project-OSRM/osrm-backend)

# > o mapa utilizado foi extraído do Projeto Open Street Map (https://download.geofabrik.de/south-america/brazil/sudeste.html)

# In[1]:


#-----------------------------------------------TIME
def TimeOSRM(lat1, lon1, lat2, lon2):
    
    import osrm
    
    s = osrm.Client(host='http://localhost:5000',timeout=10000000)

    r = s.route(
        coordinates=[[lon1,lat1], [lon2,lat2]],
        overview=osrm.overview.full)

    t = round(((r["routes"][0]["duration"])/60),2)       
    
    return t

#-----------------------------------------------DISTANCE

def DistanceOSRM(lat1, lon1, lat2, lon2):
    
    import osrm
    
    s = osrm.Client(host='http://localhost:5000',timeout=10000000)
    r = s.route(
        coordinates=[[lon1,lat1], [lon2,lat2]],
        overview=osrm.overview.full)

    d = round(((r["routes"][0]["distance"])/1000),2)
    
    return d


# ### 2) Exportação do arquivo .csv

# In[2]:


import pandas as pd

f = pd.DataFrame(pd.read_csv('time.distance.matrix.input.csv',sep=";"))
vd = []
vt = []

for i in range(0,len(f['ORIGEM_LAT'])):
    vd.append(DistanceOSRM((f['ORIGEM_LAT'].values[i]),(f['ORIGEM_LON'].values[i]),(f['DESTINO_LAT'].values[i]),(f['DESTINO_LON'].values[i])))
    vt.append(TimeOSRM((f['ORIGEM_LAT'].values[i]),(f['ORIGEM_LON'].values[i]),(f['DESTINO_LAT'].values[i]),(f['DESTINO_LON'].values[i])))
    
f['DISTANCE'] = vd
f['TIME'] = vt

f.to_csv('time.distance.matrix.csv',sep=';')

