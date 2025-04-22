from matplotlib import pyplot as plt
import geopandas as gpd
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world.plot()
plt.show()