import numpy as np
import pandas as pd

from matplotlib.cm import get_cmap
import matplotlib.colors as colors_plt
from matplotlib.colors import ListedColormap
from matplotlib import gridspec
from matplotlib.patches import Patch

import matplotlib.pyplot as plt
#%matplotlib inline 

# Assuming dist_df is your DataFrame and it includes columns "PC1", "PC2", "PC3", and "city"

# Set the figure size and create a 3D subplot
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111, projection='3d')

# Define a dictionary mapping cities to marker styles
city_markers = {
    'accra': 'o',  # Example: Circle
    'dakar': '^',  # Example: Triangle
    'des': 's',
    'kigali':'*' # Example: Square
    # Add more cities and markers as needed
}

# Iterate over the DataFrame and plot each city with its respective marker
for (city, marker), labs in zip(city_markers.items(),['Accra','Dakar', 'Dar es Salaam', 'Kigali']):
    # Select rows where the city matches
    subset = dist_df[dist_df['city'] == city]
    # Plot these rows with the specified marker
    ax.scatter(subset['PC1'], subset['PC2'], subset['PC3'], marker=marker, label=labs, c=subset['col'], s=200, alpha=1)

# Set labels for axes
# Set labels for axes
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('PC3')

# Show legend
ax.legend(frameon=False,labelspacing=1.5)

# Assuming 'ax' is your Axes3D object

# Hide tick labels and ticks on the x-axis
ax.set_xticklabels([])
#ax.set_xticks([])

# Hide tick labels and ticks on the y-axis
ax.set_yticklabels([])
#ax.set_yticks([])

# Hide tick labels and ticks on the z-axis
ax.set_zticklabels([])
#ax.set_zticks([])


# Show plot
plt.show()
