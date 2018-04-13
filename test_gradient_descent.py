"""
USES PRETRAINED NETWORKS.
"""

from kiwi import *

nn = tools.read("BinaryAddOne")

toBinary = lambda i: list(map(int, list('{0:032b}'.format(int(i)))))

print(
	tools.round_array(nn(toBinary(0)))
)