#!/usr/bin/env python

'''
	@file main.py
	@author f4rr3ll
	@brief main execution starts here
'''

# standard modules/libs
from sys import (version)

# custom modules/libs
from game.Game import Game

def main():
	print("Python version being used : {}".format(version))

	# starting the game instance
	game_i = Game()
	game_i.set_resolution((800, 600))

	# run the main game loop
	game_i.run()

	return 0

if __name__ == '__main__':
	main()
