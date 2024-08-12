import numpy as np
import pandas as pd
import altair as alt

from scipy import stats
import seaborn as sns
import geopandas as gp
from mycolorpy import colorlist as mcp

import matplotlib.pyplot as plt
#%matplotlib inline

col_dict = {'accra0': '#708090', 'accra1': '#d3d3d3', 'accra2': '#6b8e23', 'accra3': '#696969', 'accra4': '#006400', 'accra5': '#808000', 'accra6': '#9e9e9e', 'accra7': '#0000ff',
            'dakar0': '#d3d3d3', 'dakar1': '#d2b48c', 'dakar2': '#696969', 'dakar3': '#9e9e9e', 'dakar4': '#708090', 'dakar5': '#808000', 'dakar6': '#006400', 'dakar7': '#6b8e23',
            'des0': '#d3d3d3', 'des1': '#6b8e23', 'des2': '#808000', 'des3': '#708090', 'des4': '#9acd32', 'des5': '#696969', 'des6': '#BFBF00', 'des7': '#006400',
            'kigali0': '#d3d3d3', 'kigali1': '#BFBF00', 'kigali2': '#006400', 'kigali3': '#808000', 'kigali4': '#708090', 'kigali5': '#9acd32', 'kigali6': '#6b8e23', 'kigali7': '#696969'}

def prep(city, lb, geo):
    source = pd.DataFrame(geo[lb].value_counts(normalize=True).mul(100).round(1))
    source['value_count'] = source.index
    source['value_count'] = city + source['value_count'].astype(str)
    source['val_c'] = source['value_count'].map(col_dict)
    return source

a = prep('accra', 'k8_sep_lr000001_2', ac2)
dak = prep('dakar', 'k8_sep_lr000001', da)
des = prep('des', 'k8_sep_lr000001', de)
kig = prep('kigali', 'k8_sep_lr000001', ki)

accra = alt.Chart(a,  title="Accra").encode(
    theta=alt.Theta("k8_sep_lr000001_2:Q", stack=True),
    radius=alt.Radius("k8_sep_lr000001_2", scale=alt.Scale(type="sqrt", zero=True, rangeMin=20)),
    color=alt.Color("val_c:N", scale=None)).properties(
    width=500,
    height=500
)

c1 = accra.mark_arc(innerRadius=20, stroke="#fff")
c2 = accra.mark_text(radiusOffset=10).encode(text="k8_sep_lr000001_2:Q")

c1+c2

dakar = alt.Chart(dak, title="Dakar").encode(
    theta=alt.Theta("k8_sep_lr000001:Q", stack=True),
    radius=alt.Radius("k8_sep_lr000001", scale=alt.Scale(type="sqrt", zero=True, rangeMin=20)),
    color=alt.Color("val_c:N", scale=None)).properties(
    width=500,
    height=500
)

c3 = dakar.mark_arc(innerRadius=20, stroke="#fff")
c4 = dakar.mark_text(radiusOffset=10).encode(text="k8_sep_lr000001:Q")
c3+c4

dess = alt.Chart(des, title='Dar es Salaam').encode(
    theta=alt.Theta("k8_sep_lr000001:Q", stack=True),
    radius=alt.Radius("k8_sep_lr000001", scale=alt.Scale(type="sqrt", zero=True, rangeMin=20)),
    color=alt.Color("val_c:N", scale=None)).properties(
    width=500,
    height=500
)

c5 = dess.mark_arc(innerRadius=20, stroke="#fff")
c6 = dess.mark_text(radiusOffset=10).encode(text="k8_sep_lr000001:Q")
c5+c6

kigali = alt.Chart(kig, title='Kigali').encode(
    theta=alt.Theta("k8_sep_lr000001:Q", stack=True),
    radius=alt.Radius("k8_sep_lr000001", scale=alt.Scale(type="sqrt", zero=True, rangeMin=20)),
    color=alt.Color("val_c:N", scale=None)).properties(
    width=500,
    height=500
)

c7 = kigali.mark_arc(innerRadius=20, stroke="#fff")
c8 = kigali.mark_text(radiusOffset=10).encode(text="k8_sep_lr000001:Q")

c7 + c8
