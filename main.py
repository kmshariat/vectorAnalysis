import numpy as np

#component function gives us the x_component and y_component of a vector.
def component(magnitude, theta):
    x_comp = magnitude*np.cos(theta)
    y_comp = magnitude*np.sin(theta)
    print(f"V_X {x_comp} and V_y {y_comp}")


def scale(magnitude, theta, scalingFactor):
    x_comp = scalingFactor*magnitude*np.cos(theta)
    y_comp = scalingFactor*magnitude*np.sin(theta)
    print(f"({x_comp}, {y_comp}) is the new tip of the vector")
