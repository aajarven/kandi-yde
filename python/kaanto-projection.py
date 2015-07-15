# -*- coding: utf-8 -*-

import yt
import numpy as np
import math

def yksikkovektori (alpha, beta):
    return [np.cos(alpha)*np.sin(beta), np.cos(alpha)*np.sin(alpha), np.sin(alpha)]


ds = yt.load("/data/scratch3/extragal/Enzo/data/LWIR/RD0076/RD0076")
v, tiheysmaksimi = ds.find_max("density")

# katselusuunnan suuntavektorin kulma xy-tason kanssa
alpha=-np.pi

# katselusuunnan suuntavektorin projektion xy-tasolle kulma x-akselin kanssa
beta=0

# Our "width" is the width of the image plane as well as the depth.
# The first element is the left to right width, the second is the
# top-bottom width, and the last element is the back-to-front width
# (all in code units)
W = [0.04,0.04,0.4]

# The number of pixels along one side of the image.
# The final image will have Npixel^2 pixels.
Npixels = 512

frame = 1
stepAlpha=np.pi/100
stepBeta=np.pi/100
frames=math.ceil(2*np.pi/stepAlpha)

for i in np.arange(0, frames):
    L = yksikkovektori(alpha, beta)
    N = yksikkovektori(alpha+stepAlpha, beta+stepBeta)
    # Now we call the off_axis_projection function, which handles the rest.
    # Note that we set no_ghost equal to False, so that we *do* include ghost
    # zones in our data.  This takes longer to calculate, but the results look
    # much cleaner than when you ignore the ghost zones.
    # Also note that we set the field which we want to project as "density", but
    # really we could use any arbitrary field like "temperature", "metallicity"
    # or whatever.
    image = yt.off_axis_projection(ds, tiheysmaksimi, L, W, Npixels, "density", north_vector=N, no_ghost=False, steady_north=True)

    

    # Image is now an NxN array representing the intensities of the various pixels.
    # And now, we call our direct image saver.  We save the log of the result.
    #yt.write_projection(image, "slice/kaanto/offaxis_projection_colorbar%04i.png" %frame, colorbar_label="Column Density (cm$^{-2}$)")
    yt.write_projection(image, "kuvat/%04i.png" %frame, cmap_name='hot')
    
    frame+=1
    alpha+=stepAlpha
    beta+=stepBeta
    
    
    

