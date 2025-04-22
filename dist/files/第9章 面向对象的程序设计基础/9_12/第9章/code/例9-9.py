from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
map_1 = Basemap()
map_1.drawcoastlines()
plt.show()
plt.savefig('/第9章/data/test.jpg')