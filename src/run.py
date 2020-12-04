
from utils.write_airfoil import write_airfoil
from utils.NURBS import NURBS

k = {
    "ta_u":  0.9236,
    "ta_l":  0.9787,
    "tb_u":  1.1398,
    "tb_l":   1.1388,
    "alpha_b":  1.0144,
    "alpha_c": 1.0130
}

airfoil_name = 'def'

airfoil_coordinates = NURBS(k).spline()

write_airfoil(airfoil_name, airfoil_coordinates)
