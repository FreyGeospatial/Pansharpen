# Pansharpen
This is my open source alternative to the TerrSet/Idrisi PANSHARPEN module, using an intensity-hue-saturation (IHS) method.

Pansharpening is often used to increase the spatial resolution of remotely sensed imagery by fusing the higher resolution panchromatic band to the lower resolution multispectral imagery.

My code attempts to follow the high level overview of the module found in the TerrSet help guide. Though it succeeds in sharpening the image, it does not create a replica of TerrSet's output on identical data. Therefore, I consider this code to be under development, and I do not believe it is production ready until I am able to either fix these discrepencies. Any suggestions or tips are encouraged.

Sample Landsat data can be obtained from: https://clarklabs.org/download/