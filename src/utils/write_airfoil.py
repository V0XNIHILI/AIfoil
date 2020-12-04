import numpy as np

from aeropy.xfoil_module import find_coefficients, create_input


def get_coords_plain(argv):
    x_l = argv[0]
    y_l = argv[1]
    x_u = argv[2]
    y_u = argv[3]

    ycoords = np.append(y_l[::-1], y_u[1:])
    xcoords = np.append(x_l[::-1], x_u[1:])

    coordslist = np.array((xcoords, ycoords)).T
    coordstrlist = ["{:.6f} {:.6f}".format(coord[1], coord[0])
                    for coord in coordslist]

    return '\n'.join(coordstrlist)


def write_airfoil(name, airfoil_coordinates):
    with open(name, 'w') as f:
        f.write(name + '\n' + get_coords_plain(airfoil_coordinates))
