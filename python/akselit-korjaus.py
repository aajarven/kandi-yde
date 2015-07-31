elif isinstance(plot, ProfilePlot):
    subplot = plot.axes.values()[0] # siirra muualle?
    # limits for axes
    xlimits = subplot.get_xlim()
    _xrange = (YTQuantity(xlimits[0], 'm'), YTQuantity(xlimits[1], 'm')) # unit hardcoded but afaik it is not used anywhere so it doesn't matter
    if list(plot.axes.ylim.viewvalues())[0][0] is None: #mieti tata, etsi parempi tapa
         ylimits = subplot.get_ylim()
    else:
         ylimits = list(plot.axes.ylim.viewvalues())[0]
        _yrange = (YTQuantity(ylimits[0], 'm'), YTQuantity(ylimits[1], 'm')) # unit hardcoded but afaik it is not used anywhere so it doesn't matter
    # axis labels
    xaxis = subplot.xaxis
    _xlabel = pyxize_label(xaxis.label.get_text())
    yaxis = subplot.yaxis
    _ylabel = pyxize_label(yaxis.label.get_text())
    # set log if necessary
    if subplot.get_xscale() == "log":
         _xlog = True 
    else:
         _xlog = False
    if subplot.get_yscale() == "log":
         _ylog = True 
    else:
         _ylog = False
    _tickcolor = None 
