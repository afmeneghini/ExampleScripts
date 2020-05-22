# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:36:50 2020
@author: Aaron
Update the bounding box, the directory name, and the output folder for the new translated images

"""

#useful libraries
import gdal, rasterio, os, sys, geopandas as gpd, rasterio.plot as plot, pycrs
from shapely.geometry import box
from fiona.crs import from_epsg
from rasterio.mask import mask

#directories containing raster images and the output directories
dir_name = "E:\\Working\\"
out_image = "E:\\Output\\"
files = os.listdir(dir_name)

#bounding WGS coordinates for the study to clip to - if you don't need to clip
# you can use the current extents of the rasters by replacing values with min
#and max x and y variables.
minx, miny = -71.083924, 42.977764
maxx, maxy = -66.949895, 47.459686

bbox = box(minx, miny, maxx, maxy)

#raster data type / format information - driver and outgoing refer to output raster type
#specify the incoming data format
driver = "RST"
incoming = ".bil"
outgoing = ".rst"

#accessing the geodataframe or the bounding box in WGS 84
geo = gpd.GeoDataFrame({'geometry': bbox}, index=[0], crs=from_epsg(4326))

def getFeatures(gdf):
    """Function to parse features from GeoDataFrame in such a manner that rasterio wants them"""
    import json
    return [json.loads(gdf.to_json())['features'][0]['geometry']]

#iterate through input rasters
for f in os.listdir(dir_name):
    if (f.endswith(incoming)):
        print(f)

        raster = dir_name+f
        print(raster)
        i = rasterio.open(raster)
        
        #plot.show((i, 1), cmap = "terrain")
        
        
        # retrieving clipping coordinates
        coords = getFeatures(geo)
        print(coords)
        print(i.driver)
        
        out_img, out_transform = mask(i, shapes=coords, crop=True)
        #copying created meta data
        out_meta = i.meta.copy()

        #updated meta data
        out_meta.update({"driver": driver,
                         "height": out_img.shape[1],
                         "width": out_img.shape[2],
                         "transform": out_transform,
                         "crs": pycrs.parse.from_epsg_code(4326).to_proj4()
                         })
        #writing new raster image
        with rasterio.open(out_image+f[:-3]+outgoing, "w", **out_meta) as dest:
            dest.write(out_img)

