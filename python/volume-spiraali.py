# -*- coding: utf-8 -*-
import yt
import numpy as np
import math

ds = yt.load("data/dataset")
ad = ds.all_data()

# etsitään tihein kohta ja tiheimmän kohdan ympäristöstä suurin H2-pitoisuus
v, tiheysmaksimi = ds.find_max("density")
densSphere = ds.sphere(tiheysmaksimi, (0.5, "kpc"))
maxlocs = densSphere.quantities.max_location(("gas", "H2_fraction"))
H2max = maxlocs[2:5]

# etsitään suurimman H2-pitoisuuden sijainnin ympärillä 1 kpc sisältä suurin ja pienin H2-pitoisuus ja luodaan niiden logaritmien avulla ColorTransferFunction
H2sphere = ds.sphere(H2max, (1.0, "kpc"))
minimi, maksimi = H2sphere.quantities.extrema("H2_fraction")
tf = yt.ColorTransferFunction((np.log10(minimi), np.log10(maksimi)))
tf.add_layers(100, w=0.01, colormap="hot")

katselusuunta = [1, 1, 1]
W = 0.022 # vakio, joka määrää, kuinka laaja alue kuvassa näytetään
leveys = 512 # kuvan leveys pikseleissä

# luodaan camera-olio
cam = ds.camera(H2max, katselusuunta, W, leveys, tf, fields=["H2_fraction"], data_source=H2sphere)

frame=0
step=0.02
frames = int(math.floor(2*math.pi/step))

# zoomataan ja käännetään kameraa ja tallennetaan kuva numeroituna
for i, snapshot in enumerate(cam.zoomin(3, frames, clip_ratio=8.0)):
    cam.rotate(0.05)
    snapshot.write_png("kuvat/volume-spiraali%04i.png" %frame)
    frame += 1
