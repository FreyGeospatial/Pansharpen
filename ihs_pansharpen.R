library(raster)

# Load Landsat images
pan <- raster("Data/etm_pan.rst")
etm2 <- raster("Data/etm2.rst")
etm3 <- raster("Data/etm3.rst")
etm4 <- raster("Data/etm4.rst")

# Resample the Images to the Panchromatic Band's resolution
etm2_resample <- resample(etm2, pan, method = "bilinear")
etm3_resample <- resample(etm3, pan, method = "bilinear")
etm4_resample <- resample(etm4, pan, method = "bilinear")

# Perform multiple regression, using panchromatic band as dependent variable
regress <- lm(values(pan)~values(etm2_resample) + values(etm3_resample) + values(etm4_resample))

# Create new raster using predicted values
regress_img <- raster(ncols = pan@ncols, nrows = pan@nrows, crs = crs(etm2), ext = extent(pan))
values(regress_img) <- predict(regress)

# Find the difference between the panchromatic band and the predicted values
d <- pan - regress_img

# Add the differenced image values to the resampled bands
etm2_d <- d + etm2_resample
etm3_d <- d + etm3_resample
etm4_d <- d + etm4_resample

# "stack" the bands so they can be viewed as a composite image
ihs_stack <- stack(etm2_d, etm3_d, etm4_d)

# plot the composite image
plotRGB(ihs_stack, r = 3, g = 2, b = 1, stretch = "lin")
