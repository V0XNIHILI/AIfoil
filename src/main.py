# Copyright (c) 2019 Uber Technologies, Inc.
#
# Licensed under the Uber Non-Commercial License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at the root directory of this project.
#
# See the License for the specific language governing permissions and
# limitations under the License.


import torch

import numpy as np

import time
import os

from evograd import expectation
from evograd.distributions import Normal

from utils.NURBS import NURBS
from utils.write_airfoil import write_airfoil
from utils.xfoil import calc_polar, read_polar
from utils.get_random_string import get_random_string

# Code --------------------------------------------------------------------------------------------

re = 1000*1000
angles = [0]

npop = 30

max_iter = 30

non_converging_cd_cl = -1/71

std = 0.5  # noise standard deviation
alpha = 0.1  # learning rate

bad = []

def calc_cd_over_cl(x):
    y = 0

    k = {
        "ta_u":  x[0],
        "ta_l":  x[1],
        "tb_u":  x[2],
        "tb_l":   x[3],
        "alpha_b":  x[4],
        "alpha_c": x[5],
    }

    airfoil_name = 'temp/' + get_random_string(5)
    out_file = 'temp/' + get_random_string(5)

    airfoil_coordinates = NURBS(k).spline()

    write_airfoil(airfoil_name, airfoil_coordinates)

    calc_polar(airfoil_name, re, out_file, angles, [], True, 50, 200)

    polar = read_polar(out_file)

    if len(polar['cl']) == 0:
        y = non_converging_cd_cl
        bad.append(airfoil_name)
    else:
        y = polar['cd'][0] / polar['cl'][0]

    os.remove(airfoil_name)
    os.remove(out_file)
       
    return y


def fun(x):
    x_np = x.numpy()

    y = np.zeros(npop)

    for i in range(0, npop):
        y[i] = -(1/calc_cd_over_cl(x_np[i]) - 50)**2

    return torch.from_numpy(y)


mu = torch.tensor([0.1, 0.1, 1.0, 1.0, 1.0, 1.0], requires_grad=True)
p = Normal(mu, std)

for t in range(max_iter):
    print('Current iteration ' + str(t) + '/' + str(max_iter))
    sample = p.sample(npop)
    fitnesses = fun(sample)
    fitnesses = (fitnesses - fitnesses.mean()) / fitnesses.std()
    mean = expectation(fitnesses, sample, p=p)
    mean.backward()

    with torch.no_grad():
        mu += alpha * mu.grad
        mu.grad.zero_()

    print('Current fitness: ' + str(1/calc_cd_over_cl(mu.detach().numpy())))
    # print('step: {}, mean fitness: {:0.5}'.format(t, float(mu)))

print('')
print(mu)
print(1/calc_cd_over_cl(mu.detach().numpy()))
print(bad)
