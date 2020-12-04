## XFOIL

### Setup

When running `./xfoil`:

```bash
dyld: Library not loaded: /opt/local/lib/libgcc/libgfortran.3.dylib
  Referenced from: /Users/douwe/Projects/AIfoil/./xfoil
  Reason: image not found
[1]    81969 abort      ./xfoil help
```

Fix: 

```bash
sudo mkdir -p /opt/local/lib/libgcc/
```

```bash
sudo ln -s /usr/local/lib/python3.8/site-packages/numpy/.dylibs/libgfortran.3.dylib /opt/local/lib/libgcc/libgfortran.3.dylib

sudo ln -s /usr/local/lib/python3.8/site-packages/numpy/.dylibs/libquadmath.0.dylib /opt/local/lib/libgcc/libquadmath.0.dylib
```

### Running

```bash
./xfoil

LOAD airfoil.dat
OPER
```

## AeroPy

Run:
```
git clone https://github.com/leal26/AeroPy.git \
cd AeroPy \ 
pip install -e . 
```

## Results

tensor([0.8109, 0.8261, 1.1168, 1.1928, 1.0156, 1.0830], requires_grad=True)
98.14404432132964

re = 20*1000*1000
angles = [5]

npop = 30

max_iter = 40

non_converging_cd_cl = 0.001

std = 0.5  # noise standard deviation
alpha = 0.03  # learning rate