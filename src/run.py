
from utils.write_airfoil import write_airfoil
from utils.NURBS import NURBS

x = [1.5779, 1.1068, 1.0761, 1.5713, 0.9693, 1.1164]

k = {
    "ta_u":  x[0],
    "ta_l": x[1],
    "tb_u":x[2],
    "tb_l":  x[3],
    "alpha_b":x[4],
    "alpha_c": x[5],
}

# 1.0021, 1.1494, 1.3733, 1.2558, 1.1573, 1.1793
# 1.0786, 1.2378, 1.4097, 1.3377, 1.0886, 1.0698

airfoil_name = 'abc'

airfoil_coordinates = NURBS(k).spline()

write_airfoil(airfoil_name, airfoil_coordinates)
