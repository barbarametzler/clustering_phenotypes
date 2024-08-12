import numpy as np
import pandas as pd
import glob
from esda.moran import Moran
from pysal.lib import weights
from pysal.explore import esda
from mycolorpy import colorlist as mcp

from scipy import stats
import seaborn as sns
import geopandas as gp

from sklearn.preprocessing import StandardScaler, OneHotEncoder, RobustScaler, QuantileTransformer
from sklearn.metrics import davies_bouldin_score, calinski_harabasz_score, normalized_mutual_info_score
from sklearn.cluster import KMeans

from matplotlib.cm import get_cmap
import matplotlib.colors as colors_plt
from matplotlib.colors import ListedColormap
from matplotlib import gridspec

import matplotlib.pyplot as plt
#%matplotlib inline

def plot_map(city, gdf, df, cluster_label, img_title, na=True):
    
    mouf_n = ['area_mean', 'bui_count',  'avg_bui', 'orientation_mean',  'ndvi_mean', 'pop_mean',
    'all_length', 'major_length', 'dist_allroads', 'dist_mroads', cluster_label]
    mouf = ['area_mean', 'bui_count',  'avg_bui', 'orientation_mean',  'ndvi_mean', 'pop_mean',
    'all_length', 'major_length', 'dist_allroads', 'dist_mroads']
    labels = ['B. area', 'B. count', 'Avg. b. size', 'B. orient.', 'NDVI', 'Pop. den.', 'Dist. all roads', 'Dist. m. roads',
                   'All roads','M. roads']
        
    df[mouf] = QuantileTransformer(output_distribution='uniform').fit_transform(df[mouf])
    d = df[mouf_n].groupby(cluster_label).agg('median')
    #print(d)
    sel = d.copy()
    sel = sel.fillna(0)
    
    classes = sel['ndvi_mean'].sort_values(ascending=True).index.astype(int, copy = False).to_list() #[1,6,5,7,0,3,4,2] 

    #col= ["dimgray","lightgray","tan", "y", "yellowgreen", "olive", "olivedrab", "darkgreen"] #"lightgray" oive  "forestgreen" darkolivegreen # y -> sandybrown #tan c
    #col= ["dimgray","slategrey", "lightgray", "y", "yellowgreen", "olive", "olivedrab", "darkgreen"] #"lightgray" oive  "forestgreen" darkolivegreen # y -> sandybrown #tan c
    col = ["blue", "dimgray","slategrey", "lightgray", "yellowgreen", "olive", "olivedrab", "darkgreen"]
    #col= ["dimgray","slategrey", "lightgray","blue", "yellowgreen", "olive", "olivedrab", "darkgreen"] #"lightgray" oive  "forestgreen" darkolivegreen ##accra
    #col= ["dimgray","slategrey", "lightgray","blue", "yellowgreen", "olive", "olivedrab", "darkgreen"] #"lightgray" oive  "forestgreen" darkolivegreen #dakar
    #col= ["dimgray","slategrey",'tan', "lightgray", "yellowgreen", "olive", "olivedrab", "darkgreen"] #dakar c


    dict1 = pd.DataFrame(zip(classes, col), columns=['id', 'color'])
    dic = dict1.sort_values('id')
    color = dic['color'].to_list()
    #color =['dimgray', 'olive', 'olivedrab', 'y', 'darkgreen', 'slategrey', 'yellowgreen', 'lightgray']
    
    nbr_colors = [col[i] for i in classes]
    nbr_cmap = ListedColormap(color) #nbr_colors

    f = plt.figure(figsize=(20, 10))
    gs = gridspec.GridSpec(1, 2, width_ratios=[5, 1]) 
    ax1 = plt.subplot(gs[0])
    
    #if city == 'accra':
    #    me = pd.merge(gdf, df[['filename', cluster_label]])
    #    gdf = me.copy()
    #print(sel)   
    ci = gdf.plot(column=cluster_label, cmap=nbr_cmap, legend=True, ax=ax1)
    ax1.set(title=img_title)
    ax1.set_axis_off()

    ax2 = plt.subplot(gs[1])
    plt.rcdefaults()
    y_pos = np.arange(len(gdf[cluster_label].value_counts()))
    counts = gdf[cluster_label].value_counts()
    
    cla = [7,6,5,4,3,2,1,0]
    co = [counts[i] for i in cla]
    nbr_colors.reverse()
    #co.reverse()
    #cla = [7,6,5,4,3,2,1,0]
    color.reverse()
    
    ax2.barh(y_pos, co, color=color, align='center')
    ax2.set_yticks(y_pos) #labels=)
    ax2.invert_yaxis()  # labels read top-to-bottom
    ax2.set_xlabel('Count')
    ax2.set_title('Cluster size')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax2.get_yaxis().set_ticks([])
    plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')
    plt.show()
