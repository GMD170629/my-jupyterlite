import geopandas as gpd
import pandas as pd
from plotnine import *

df_map = gpd.GeoDataFrame.from_file('Virtual_Map1.shp')
df_city = pd.read_csv("Virtual_City.csv")

df = pd.merge(right=df_map, left=df_city, how='right', on="country")
df = gpd.GeoDataFrame(df)

# 数值映射到单个视觉通道（气泡大小）

base_plot = (ggplot(df) +
             geom_map(fill='white', color='gray') +
             geom_point(aes(x='long', y='lat', size='orange'), shape='o', colour="black", fill='#EF5439') +
             geom_text(aes(x='long', y='lat', label='city'), colour="black", size=10, nudge_y=-1.5) +
             scale_size(range=(2, 9), name='price')
             )
print(base_plot)
#数值映射到两个视觉通道（气泡大小和颜色）

base_plot=(ggplot(df)+
           geom_map(fill='white',color='gray')+
           geom_point(aes(x='long', y='lat',size='orange',fill='orange'),shape='o',colour="black")+
           geom_text(aes(x='long', y='lat', label='city'),colour="black",size=10,nudge_y=-1.5)+
          scale_fill_cmap(name="YlOrRd")+
          scale_size(range=(2,9),name='price')
)
print(base_plot)