import matplotlib.pyplot as mpl
import pandas as pd
import geopandas as gpd
import numpy as np
from Dataparsing import r_airplane

a_list = []
c_list = []

# This loop goes through every plane in the r_airplane list.
for plane_index in range(0, len(r_airplane)):  # how many altitudes are in a list and gives range

    # This loop goes through every altitude in the current plane object.
    for index in range(0, len(r_airplane[plane_index].alt)):

        # This converts the current altitude from a string into a float.
        r_airplane[plane_index].alt[index] = float(r_airplane[plane_index].alt[index])
        r_airplane[plane_index].clock[index] = float(r_airplane[plane_index].clock[index])

        # This adds the current altitude to the altitude list which will contain all the altitudes
        # for every plane.
        a_list.append(r_airplane[plane_index].alt[index])
        c_list.append(r_airplane[plane_index].clock[index])
    # This will add the current planes altitude data to the plot.
    mpl.plot(r_airplane[plane_index].clock, r_airplane[plane_index].alt)

# This will sort the altitude list into numerical order.
a_list.sort()
c_list.sort()
# This will find the maximum and minimum altitude values in the list containing all altitudes.
max_alt = a_list[len(a_list)-1]
min_alt = a_list[0]

max_clock = c_list[len(c_list)-1]
min_clock = c_list[0]

# This sets the axis range of the plot.
mpl.ylim([min_alt, max_alt])
mpl.xlim([min_clock, max_clock])

# This shows the plot.
mpl.show()


#mpl.plot(range(0, len(r_airplane[4].alt)), r_airplane[4].alt)
#mpl.show()
