# -*- coding: utf-8 -*-
import yt
import yt.visualization.eps_writer as eps
import matplotlib

sarakkeet = 2
rivit = 1
leveys = 7.0 # (kpc)
xaxis_flags = []
yaxis_flags = []
cb_location=[]
plotit = []

ds=yt.load("/data/scratch3/extragal/Enzo/data/LWIR/RD0076/RD0076")
v, tiheysmaksimi = ds.find_max("density")

# ensimmäinen kuva
tiheys = yt.SlicePlot(ds, 1, "Density", center=tiheysmaksimi, width=(leveys, 'kpc'))
tiheys.set_unit("Density", "g/cm**3")
tiheys.set_cmap(field="Density", cmap='hot')
tiheys.save("kuvat/tiheys.png")
plotit.append(tiheys)
xaxis_flags.append(0) # x-akseli alapuolelle
yaxis_flags.append(0) # y-akseli vasemmalle
cb_location.append("top") # väripalkki yläpuolelle

#toinen kuva
lampo = yt.SlicePlot(ds, 1, "Temperature", center=tiheysmaksimi, width=(leveys, 'kpc'))
lampo.set_cmap(field="Temperature", cmap='hot')
lampo.save("kuvat/lampo.png")
plotit.append(lampo)
xaxis_flags.append(0) # x-akseli alapuolelle
yaxis_flags.append(1) # y-akseli oikealle
cb_location.append("top") # väripalkki yläpuolelle

multi = eps.multiplot(sarakkeet, rivit, plotit, bare_axes=False,  xaxis_flags = xaxis_flags, yaxis_flags = yaxis_flags, cb_location=cb_location)
multi.save_fig("kuvat/EPSMultiPlot", format="png")
