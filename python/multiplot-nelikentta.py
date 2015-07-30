import yt
import pyx
import yt.visualization.eps_writer as eps
from yt.units.yt_array import YTQuantity, YTArray
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

ds = yt.load("/data/scratch3/extragal/Enzo/data/LWIR/RD0072/RD0072")
dd=ds.all_data()

sarakkeet = 2
rivit = 2
leveys = yt.YTQuantity(7.0, 'kpc')
white=pyx.color.cmyk.white
linewidth = 3
prof_xrange = [0.1, 7.0] #kpc
colorbar_label = []
plots = []
colorbar_flags = []
xaxis_flags = []
yaxis_flags = []

val, maxTiheys = ds.find_max("density")
try:
    keskusta = dd["RadiationParticle", "particle_position"][0]
except:
    print "No particle position found"
    keskusta = [0.5, 0.5, 0.5]

leftedge = keskusta - leveys/2
rightedge = keskusta + leveys/2
myregion = ds.region(keskusta, leftedge, rightedge)

#H Number Density
H_proj = yt.ProjectionPlot(ds, 1, "H_number_density", center=keskusta, width=leveys, data_source=myregion, weight_field='density')
H_proj.set_log('H_number_density', False)
H_proj.set_zlim('H_number_density', 15e-3, 6e-2)
H_proj.save("kuvat/Hproj.png")
plots.append(H_proj)
colorbar_label.append("H Number Density (cm$^{-3}$)")
colorbar_flags.append(True)
xaxis_flags.append(-1)
yaxis_flags.append(-1)

#H2 Fraction
H2_slice = yt.SlicePlot(ds, 1, "H2_fraction", center=keskusta, width=leveys, north_vector = [1,0,0])
H2_slice.set_zlim('H2_fraction', 1e-11, 8e-6)
H2_slice.save("kuvat/H2fracproj.png")
plots.append(H2_slice)
colorbar_label.append("H$_2$ Fraction")
colorbar_flags.append(True)
xaxis_flags.append(-1)
yaxis_flags.append(-1)

#H profile
sphere = ds.sphere(maxTiheys, leveys)
H_prof = yt.ProfilePlot(sphere, "radius", ["H_number_density"])
H_prof.set_unit("radius", "kpc")
H_prof.set_xlim(prof_xrange[0], prof_xrange[1])
H_prof.set_ylim("H_number_density", 0.015, 0.13)
H_prof.set_line_property("linewidth", linewidth)
H_prof.x_log = False
H_prof.save("kuvat/Hprof.png")
plots.append(H_prof)
colorbar_flags.append(False)
xaxis_flags.append(0)
yaxis_flags.append(0)

#H2 profile
sphere = ds.sphere(keskusta, leveys)
H2_prof = yt.ProfilePlot(sphere, "radius", ["H2_fraction"])
plots.append(H2_prof)
colorbar_flags.append(False)
xaxis_flags.append(0)
yaxis_flags.append(1)
H2_prof.save("kuvat/H2prof.png")

multi = eps.multiplot(sarakkeet, rivit, plots, bare_axes=False, cb_labels=colorbar_label, cb_flags = colorbar_flags, xaxis_flags = xaxis_flags, yaxis_flags = yaxis_flags)
multi.scale_line(label="%.1f kpc" % (0.5*leveys),size=0.5, loc=(0.05,1.08))
multi.title_box("z = %2.6f" % (ds.current_redshift), loc=(0.1,1.95), 
color=white, bgcolor=None, text_opts=[pyx.text.size.large])
multi.save_fig("kuvat/nelikko", format="png")
