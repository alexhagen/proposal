import sys
sys.path.append("/home/ahagen/code");
from pym import func as ahm
from pyg import twod as ahp

# import points from john_muir_trail_elevation.txt

# make a curve out of these
jmt = ahm.curve(mileage,elevation,name="John Muir Trail Elevation");

# Plot this elevation to one line
jmt_plot = jmt.plot();

# add in points of interest

# export
plot.export('john_muir_trail_plan',formats=['png','pgf'],sizes=['cs'],customsize=[7.4,4]);
