import numpy as np

#this returns the magnitude of a vector ai+bj+ck
def magnitude(i,j,k):
    return np.sqrt(i**2+j**2+k**2)

#this returns the angle between the vector and the axes
def angle(i,j,k):
    alpha = np.arccos(i/np.sqrt(i**2+j**2+k**2))*(180/np.pi)
    beta = np.arccos(j/np.sqrt(i**2+j**2+k**2))*(180/np.pi)
    gamma = np.arccos(k/np.sqrt(i**2+j**2+k**2))*(180/np.pi)
    angles = [alpha, beta, gamma]
    return angles 

#this returns the sum of two vectors
def sum(i1, j1, k1, i2, j2, k2):
    return str(i1+i2)+'i '+str(j1+j2)+'j '+ str(k1+k2)+'k '

#this returns the unit vector
def unit(i,j,k):
    return str(i/np.sqrt(i**2+j**2+k**2))+'i '+ str(j/np.sqrt(i**2+j**2+k**2)) + 'j '+ str(k/np.sqrt(i**2+j**2+k**2))+ 'k '
print(unit(2,-6,-3))

#component function gives us the x_component and y_component of a vector.
def component(magnitude, theta):
    theta = theta*(np.pi/180)
    x_comp = magnitude*np.cos(theta)
    y_comp = magnitude*np.sin(theta)
    comp = [x_comp, y_comp]
    return comp

#scaling the whole vector
def scale(magnitude, theta, scalingFactor):
    theta = theta*(np.pi/180)
    x_comp = scalingFactor*magnitude*np.cos(theta)
    y_comp = scalingFactor*magnitude*np.sin(theta)
    new_tip = [x_comp, y_comp]
    return new_tip 

#this xscale function only scale in the x axis
def xscale(magnitude, theta, xscalingfactor):
    theta = theta*(np.pi/180)
    x_comp = xscalingfactor*magnitude*np.cos(theta)
    y_comp = magnitude*np.sin(theta)
    new_tip = [x_comp, y_comp]
    return new_tip
    
#this yscale function only scale in the y axis
def yscale(magnitude, theta, yscalingfactor):
    theta = theta*(np.pi/180)
    x_comp = magnitude*np.cos(theta)
    y_comp = yscalingfactor*magnitude*np.sin(theta)
    new_tip = [x_comp, y_comp]
    return new_tip

# resultant of two vectors when magnitude of both of them and angle between them is given
def resultant(magnitude1, magnitude2, alpha):
    alpha = alpha*(np.pi/180)
    resultant = np.sqrt(magnitude1**2 + magnitude2**2 + 2*magnitude1*magnitude2*np.cos(alpha))
    return resultant

#this angleofR function returns the angle of the resultant vector with respect to first vector
def angleofR(magnitude1, magnitude2, alpha):
    alpha = alpha*(np.pi/180)
    theta = np.arctan((magnitude2*np.sin(alpha))/(magnitude1 + magnitude2*np.cos(alpha)))*(180/np.pi)
    return theta
