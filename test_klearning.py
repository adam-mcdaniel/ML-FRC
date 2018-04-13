"""
USES PRETRAINED NETWORKS.
"""

from klearning import *
from kiwi.tools import *
from kiwi.reinforcement import Agent
from kiwi.reinforcement import KiwiLearning

def main():
	bee = Bee()
	k = read("Learning")

	k.out_functions = [bee.moveLeft,
					   bee.moveRight,
					   bee.moveUp,
					   bee.moveDown]

	for i in range(20):
		k.update(bee.state)
		print(bee.state)


if __name__ == "__main__":
	main()