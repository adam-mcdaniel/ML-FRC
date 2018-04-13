"""
TRAINS A GRADIENT DESCENT NEURAL
NETWORK WITH ONLY ONE HIDDEN LAYER.
"""

from kiwi import *

batches = 2000

in_ = model.Dataset(32)
out_ = model.Dataset(32)

toBinary = lambda i: list(map(int, list('{0:032b}'.format(int(i)))))

for i in range(batches):
    in_.add(toBinary(i))
    out_.add(toBinary(i+1))

nn = regression.GradientDescent(
    in_(),
    out_()
)

tools.save(nn, "BinaryAddOne")

for i in range(0, 10):
    print("nn={}, real={}".format(tools.round_array(nn(toBinary(i))), toBinary(i)))