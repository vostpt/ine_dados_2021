# -*- coding: utf-8 -*-
# Original Code by Jorge Gomes for VOST Portugal

# -----------------------------------------------
#                  LIBRARIES
# -----------------------------------------------

import geopandas as gpd
import pandas as pd 
import plotly.express as px 

# -----------------------------------------------
#                 DATA TREATMENT
# -----------------------------------------------

# Read geojson file
gdf = gpd.read_file('nelas_geo.geojson')

# Change geojson format 
gdf.to_crs(epsg=4326, inplace=True)

# Set index column to BGRI2021
gdf.set_index('BGRI2021', inplace=True)

# -----------------------------------------------
#                 DESIGN MAP 
# -----------------------------------------------

# Calculate map and stylize

fig = px.choropleth_mapbox(gdf,
                        geojson=gdf['geometry'], # geojson source
                        locations=gdf.index,	 # common point to get information from 
                        color='N_INDIVIDUOS_RESIDENT',	# what column to use for scale 
                        color_continuous_scale="Blues",	# what color to use for scale 
                        mapbox_style="open-street-map",	# what kind of base map 
                        center={'lat':40.54047095284935, 'lon':-7.8506492725422055}, # where to center the map 
                       	zoom=10,	# zoom applied to map 
						opacity=0.8,	#opacity for the layers	
						height=900	# Map height in pixels
                        )
# Show Map 
fig.show()


# -----------------------------------------------
#              APP ENDS HERE
# -----------------------------------------------

# Thanks to R-Beginners for the explanation regarding different projection formats 
# https://stackoverflow.com/questions/71923114/cant-make-px-choropleth-mapbox-to-draw-multipolygon/71925649?noredirect=1#comment127098083_71925649
