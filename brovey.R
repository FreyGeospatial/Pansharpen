library(raster)

# Load Landsat images
pan <- raster("Data/etm_pan.rst")
etm2 <- raster("Data/etm2.rst")
etm3 <- raster("Data/etm3.rst")
etm4 <- raster("Data/etm4.rst")

etm2_resample <- resample(etm2, pan, method = "bilinear")
etm3_resample <- resample(etm3, pan, method = "bilinear")
etm4_resample <- resample(etm4, pan, method = "bilinear")

mul_avg <- (etm2_resample + etm3_resample + etm4_resample) / 3

brovey_2 <- pan / mul_avg * etm2_resample
brovey_3 <- pan / mul_avg * etm3_resample
brovey_4 <- pan / mul_avg * etm4_resample

brovey_stack <- stack(brovey_2, brovey_3, brovey_4)

plotRGB(brovey_stack, r = 3, g = 2, b = 1, stretch = "lin")
writeRaster(brovey_2, "data/brovey_2.rst", overwrite=T)
writeRaster(brovey_3, "data/brovey_3.rst", overwrite=T)
writeRaster(brovey_4, "data/brovey_4.rst", overwrite=T)
