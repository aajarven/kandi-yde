# -*- coding: utf-8 -*-

import yt
import numpy as np

ds = yt.load("data/dataset")
v, maxtiheys = ds.find_max("density")
frame = 0

for i in np.arange(-0.5, 0.5, 0.01):
    siirto = yt.YTArray([0, 0, i], 'kpc')
    keskusta = maxtiheys - siirto
    
    image = yt.SlicePlot(ds, 'z', center=keskusta, fields=['density'], width=(3, 'kpc'))
    image.set_zlim('density', 3e-26, 25e-26)
    image.set_cmap("density", "hot")
    image.set_font_size(35)
    image.save("kuvat/flythrough/%04i.png" %frame)
    frame+=1
