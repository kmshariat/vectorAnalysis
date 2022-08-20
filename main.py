import numpy as np

# this returns the magnitude of a vector ai+bj+ck
def magnitude(i, j, k):
    return np.sqrt(i**2 + j**2 + k**2)


# this returns the angle between the vector and the axes
def angle(*vec):
    mag = magnitude(*vec)
    return [np.rad2deg(np.arccos(x / mag)) for x in vec]


def str_vec(x, y, z):
    return f"{x}î + {y}ĵ + {z}k̂"


# this returns the sum of two vectors
def sum(i1, j1, k1, i2, j2, k2):
    return str_vec(i1 + i2, j1 + j2, k1 + k2)


# this returns the unit vector
def unit(i, j, k):
    v = np.array([i, j, k])
    mag = magnitude(*v)
    return str_vec(*(v / mag if mag != 0 else v))


print(unit(2, -6, -3))

# this returns the dot product of two vectors
def dot(i1, j1, k1, i2, j2, k2):
    return i1 * i2 + j1 * j2 + k1 * k2


# this returns the cross product of two vectors
def cross(i1, j1, k1, i2, j2, k2):
    return str_vec(j1 * k2 - k1 * j2, -1 * (i1 * k2 - k1 * i2), i1 * j2 - i2 * j1)


print(cross(2, -3, -1, 1, 4, -2))

# angle between two vectors a and b
def angleoftwo(i1, j1, k1, i2, j2, k2):
    angle = np.rad2deg(
        np.arccos(
            dot(i1, j1, k1, i2, j2, k2)
            / (magnitude(i1, j1, k1) * magnitude(i2, j2, k2))
        )
    )
    return angle


# projection of a vector
def projection(i1, j1, k1, i2, j2, k2):
    proj_ab = dot(i1, j1, k1, i2, j2, k2) / magnitude(
        i2, j2, k2
    )  # this is the projection of a onto b
    proj_ba = dot(i2, j2, k2, i1, j1, k1) / magnitude(
        i1, j1, k1
    )  # this is the projection of b onto a
    projection = [proj_ab, proj_ba]
    return projection


# component function gives us the x_component and y_component of a vector.
def component(magnitude, theta):
    theta = np.deg2rad(theta)
    x_comp = magnitude * np.cos(theta)
    y_comp = magnitude * np.sin(theta)
    comp = [x_comp, y_comp]
    return comp


# scaling the whole vector
def scale(magnitude, theta, scalingFactor):
    theta = np.deg2rad(theta)
    x_comp = scalingFactor * magnitude * np.cos(theta)
    y_comp = scalingFactor * magnitude * np.sin(theta)
    new_tip = [x_comp, y_comp]
    return new_tip


# this xscale function only scale in the x axis
def xscale(magnitude, theta, xscalingfactor):
    theta = np.deg2rad(theta)
    x_comp = xscalingfactor * magnitude * np.cos(theta)
    y_comp = magnitude * np.sin(theta)
    new_tip = [x_comp, y_comp]
    return new_tip


# this yscale function only scale in the y axis
def yscale(magnitude, theta, yscalingfactor):
    theta = np.deg2rad(theta)
    x_comp = magnitude * np.cos(theta)
    y_comp = yscalingfactor * magnitude * np.sin(theta)
    new_tip = [x_comp, y_comp]
    return new_tip


# resultant of two vectors when magnitude of both of them and angle between them is given
def resultant(magnitude1, magnitude2, alpha):
    alpha = np.deg2rad(alpha)
    resultant = np.sqrt(
        magnitude1**2 + magnitude2**2 + 2 * magnitude1 * magnitude2 * np.cos(alpha)
    )
    return resultant


# this angleofR function returns the angle of the resultant vector with respect to first vector
def angleofR(magnitude1, magnitude2, alpha):
    alpha = np.deg2rad(alpha)
    theta = np.rad2deg(
        np.arctan(
            (magnitude2 * np.sin(alpha)) / (magnitude1 + magnitude2 * np.cos(alpha))
        )
    )
    return theta
