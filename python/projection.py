# -*- coding: utf-8 -*-

import yt

ds = yt.load("/data/scratch3/extragal/Enzo/data/LWIR/RD0076/RD0076")

v, keskusta = ds.find_max("density")
vasen_kulma = keskusta + yt.YTArray([-1.5, -1.5, -0.5], 'kpc') 
oikea_kulma = keskusta + yt.YTArray([1.5, 1.5, 0.5], 'kpc')
region = ds.box(vasen_kulma, oikea_kulma)

plot = yt.ProjectionPlot(ds, 'z', fields=['density'], center='max', data_source = region, width=(3, 'kpc'))
plot.set_zlim("density", 8e-4, 1e-4)
plot.set_cmap("density", "hot")
plot.set_font_size(30)
plot.save("kuvat/projection.png")
