import sys
sys.path.append("/home/ahagen/code");
from pym import func as ahm
from pyg import twod as ahp
import numpy as np

# import points from john_muir_trail_elevation.txt
arr = np.loadtxt('john_muir_trail_elevation.txt',delimiter=',');

mileage = arr[:,0];
elevation = arr[:,1];

# make a curve out of these
jmt = ahm.curve(mileage,elevation,name="John Muir Trail Elevation");

# Plot this elevation to one line
jmt_plot = jmt.plot(linecolor='#ff0000',linestyle='-');
jmt_plot.lines_on();
jmt_plot.markers_on();
jmt_plot.xlabel('Distance ($s$) [$mi$]');
jmt_plot.ylabel('Elevation ($z$) [$ft$]');
# add in points of interest

# export
jmt_plot.export('john_muir_trail_plan',formats=['png','pgf'],sizes=['cs'],customsize=[7.4,2.]);
