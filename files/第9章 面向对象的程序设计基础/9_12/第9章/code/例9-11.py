import geopandas as gpd
import pandas as pd
from plotnine import *

df_map = gpd.GeoDataFrame.from_file('Virtual_Map1.shp')
df_city=pd.read_csv("Virtual_City.csv")
df=pd.merge(right=df_map, left=df_city,how='right',on="country")
df=gpd.GeoDataFrame(df)

#标准点描法地图
base_plot=(ggplot(df)+
           geom_map(fill='white',color='gray')+
           geom_point(aes(x='long', y='lat'),shape='o',colour="black",size=6,fill='r')+
           geom_text(aes(x='long', y='lat', label='city'),colour="black",size=10,nudge_y=-1.5)+
          scale_fill_cmap(name="RdYlBu_r")
)
print(base_plot)
#标签型点描法地图
base_plot=(ggplot(df)+
           geom_map(fill='white',color='gray')+
           geom_label(aes(x='long', y='lat', label='city'),colour="black",size=10,fill='orange')+
          scale_fill_cmap(name="RdYlBu_r")
)
print(base_plot)
