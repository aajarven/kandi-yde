# -*- coding: utf-8 -*-

import yt
import numpy as np
import math

ds = yt.load("/data/scratch3/extragal/Enzo/data/LWIR/RD0076/RD0076")
ad = ds.all_data()

v, tiheysmaksimi = ds.find_max("density")
#print tiheysmaksimi
densSphere = ds.sphere(tiheysmaksimi, (0.5, "kpc"))
maxlocs = densSphere.quantities.max_location(("gas", "H2_fraction"))
#print maxlocs
H2max = maxlocs[2:5]
#print H2max
H2sphere = ds.sphere(H2max, (1.5, "kpc"))

mi, ma = H2sphere.quantities.extrema("H2_fraction")
tf = yt.ColorTransferFunction((np.log10(mi), np.log10(ma)))
tf.add_layers(100, w=0.01, colormap="hot")

L = [1, 1, 1]
W = 0.04
Npixels = 512

cam = ds.camera(H2max, L, W, Npixels, tf, fields=["H2_fraction"], data_source=H2sphere)
	
frame=0
step=0.02
frames = int(math.floor(2*math.pi/step))

for i, snapshot in enumerate(cam.zoomin(7, frames, clip_ratio=8.0)):
    cam.rotate(0.05)
    #snapshot.write_png("../kuvat/volume/spiraali/H2_frac/H2frac-%04i.png" % frame, clip_ratio=8.0)
    cam.save_annotated("../kuvat/volume/spiraali/H2_frac/1500pc/%04i.png" %frame, snapshot)
    frame += 1
