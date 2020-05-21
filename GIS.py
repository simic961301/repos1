#!/usr/bin/env python
# coding: utf-8

# Работа с веб-картами по какой-то причине не доступна, объекты не грузятся.

# In[58]:


from arcgis.mapping import WebMap
empty_webmap = WebMap()


# In[59]:


empty_webmap.layers


# In[61]:


ebola_map = WebMap(ebola_map_item)


# # Модуль arcgis.mapping

# Использование виджета карты

# In[4]:


import arcgis
from arcgis.gis import GIS


# In[5]:


gis = GIS()


# Создание виджета карты

# In[8]:


map1 = gis.map('Moscow')


# In[17]:


map1


# Масшатабирование, вращение и центрирование

# In[18]:


map1.zoom


# In[20]:


map1.zoom = 10


# In[21]:


map1.rotation = 45


# In[66]:


map2 = gis.map()
map2


# In[67]:


map2.center


# # Smart Mapping

# Визуализация данных о местоположении. Тепловой карта визуализации землетрясений.

# In[28]:


map3 = gis.map('Los Angeles', 8)


# In[29]:


map3


# In[32]:


map3.add_layer({"type":"FeatureLayer",
                "url":"http://services1.arcgis.com/hLJbHVT9ZrDIzK0I/arcgis/rest/services/EQMagGt4/FeatureServer/0",
                "renderer":"HeatmapRenderer", "opacity":0.75})


# Визуализация особенностей области. Населенность округов штата.

# In[55]:


map4 = gis.map('New York, NY', 6)


# In[56]:


map4


# In[57]:


map4.add_layer({"type":"FeatureLayer",

"url":"//sampleserver6.arcgisonline.com/arcgis/rest/services/Census/MapServer/2",
 "definition_expression" : "STATE_NAME='New York'",
 "renderer":"ClassedColorRenderer",
 "field_name":"POP2007",
 "opacity":0.7
 })


# In[ ]:




