import pandas as pd
import numpy as np
import rasterio
import os
from matplotlib import pyplot

# set the working directory
os.chdir("C:/users/jfrey/documents/udemy/pansharpen/pansharpen")

# location of raster files from Landsat 7 ETM+
pan_path = "data/etm_pan.rst" # band 8 panchromatic band
etm2_path = "data/etm2.rst" # red band
etm3_path = "data/etm3.rst" # green band
etm4_path = "data/etm4.rst" # blue band

# no need to call file.close() when using `with` statement
# the .profile method opens the raster's metadata, including spatial
# resolution (e.g., panchromatic is 15m while multispectral bands are 15m)
with rasterio.open(etm2_path) as src:
    print(src.profile)
    pyplot.imshow(src.read(1), cmap = "Reds")

with rasterio.open(etm3_path) as src:
    print(src.profile)
    pyplot.imshow(src.read(1), cmap = "Greens")
    
with rasterio.open(etm4_path) as src:
    print(src.profile)
    pyplot.imshow(src.read(1), cmap = "Blues")
    
# this is easier for ad hoc scripting, though, if you
# could use tooltips from the IDE. To access help,
# type `help(<function>/<module>/<method>)`.
# E.g., `help(rasterio.open)` or `help(pan.read)`
pan = rasterio.open(pan_path)
type(pan.read) # of type rasterio.io.DatasetReader 
pan.read() # yields a matrix of values
pyplot.imshow(pan.read(1), cmap = "gray")

      
# resample data to target shape
# --note-- this can also be done using `with` statement  
def myResample(image, upscale_factor):

    # This first block resamples the image
    image_resampled = image.read(
        # `out_shape` param must be a Tuple. Describes shape of output
        # number of bands contained in image (here, it is just 1).
        out_shape = (image.count, 
                     int(image.height * upscale_factor),
                     int(image.width * upscale_factor)
                     ),
        # resampling param sets resampling method
        resampling = rasterio.enums.Resampling.bilinear)
    print('Shape before resample: ', image.shape)
    print('Shape after resample: ', image_resampled.shape[1:])
    
    # scale image. image.transform.scale will scale in both dimensions
    # equally using a scalar value. This is for the image metadata, should
    # you wish to save the image. for now, we will be satisfied with a
    # numpy.ndarray output.
    
    # image_transformed = image.transform * image.transform.scale(
    #     (image.width / image_resampled.shape[-1]),
    #     (image.height / image_resampled.shape[-2]))
    
    # image.profile.update(transform = image_transformed)
    
    # print('Transform before resample: \n', image.transform)
    # print('Transform after resample: \n', image_transformed)
    
    return image_resampled
        
etm2 = rasterio.open(etm2_path)
etm3 = rasterio.open(etm3_path)
etm4 = rasterio.open(etm4_path)

# we upscale by a factor of 2, as the panchromatic band has twice
# as fine resolution (15m) as the RGB bands (30m)
etm2_resampled = myResample(etm2, 2)
etm3_resampled = myResample(etm3, 2)
etm4_resampled = myResample(etm4, 2)
