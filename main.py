import numpy as np

#component function gives us the x_component and y_component of a vector.
def component(magnitude, theta):
    x_comp = magnitude*np.cos(theta)
    y_comp = magnitude*np.sin(theta)
    comp = [x_comp, y_comp]
    return comp

#scaling the whole vector
def scale(magnitude, theta, scalingFactor):
    x_comp = scalingFactor*magnitude*np.cos(theta)
    y_comp = scalingFactor*magnitude*np.sin(theta)
    new_tip = [x_comp, y_comp]
    return new_tip 

#this xscale function only scale in the x axis
def xscale(magnitude, theta, xscalingfactor):
    x_comp = xscalingfactor*magnitude*np.cos(theta)
    y_comp = magnitude*np.sin(theta)
    new_tip = [x_comp, y_comp]
    return new_tip
    
#this yscale function only scale in the y axis
def yscale(magnitude, theta, yscalingfactor):
    x_comp = magnitude*np.cos(theta)
    y_comp = yscalingfactor*magnitude*np.sin(theta)
    new_tip = [x_comp, y_comp]
    return new_tip

# resultant of two vectors when magnitude of both of them and angle between them is given
def resultant(magnitude1, magnitude2, alpha):
    resultant = np.sqrt(magnitude1**2 + magnitude2**2 + 2*magnitude1*magnitude2*np.cos(alpha))
    return resultant
