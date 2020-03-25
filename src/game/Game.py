'''
	@file Game.py
	@author f4rr3ll
	@brief module component containing the game code
'''

# third-party modules/libs
from pygame import (init, display, event, draw)
from pygame import (QUIT)

class Game:
	'''
		@class Game
		@brief class containing all the logic for the game
	'''
	def __init__(self):
		'''
			@function __init__
			@brief default constructor
		'''
		self.game_scr = None
		self.done = False

		init()

	def set_resolution(self, i_resolution : tuple):
		'''
			@function set_resolution
			@brief set the resolution of the screen
			@param [IN] i_resolution : tuple (width, height) containing the
			width and height of the screen to be used
		'''
		if (i_resolution is None) or (len(i_resolution) == 0):
			raise ValueError("Resolution cannot be empty")
		elif not isinstance(i_resolution, tuple):
			raise TypeError("Resolution value provided has to be a " +
					"tuple(width, height)")

		self.game_scr = display.set_mode(i_resolution)

	def run(self):
		'''
			@function run
			@brief runs the main loop of the game
		'''
		self._draw_field()
		while not self.done:
			for evt in event.get():
				if evt.type == QUIT:
					self.done = True

			self._update()

	def _draw_field(self):
		'''
			@function draw_field
			@brief function to draw the playing field of the game
		'''
		# first get the screen resolution set
		w, h = self.game_scr.get_size()
		print("Screen size set : {}".format((w, h)))

		# now draw the vertical lines
		draw.line(self.game_scr, (255, 255, 255), (270, 10), (270, w-10))
		draw.line(self.game_scr, (255, 255, 255), (h - 50, 10), (h - 50, w-10))

		# now draw the horizontal lines
		draw.line(self.game_scr, (255, 255, 255), (10, 200), (w - 10, 200))
		draw.line(self.game_scr, (255, 255, 255), (10, h - 170),
				(w - 10, h - 170))

		# figure out the regions of the boxes

	def _update(self):
		'''
			@function update
			@brief update logic
		'''
		display.flip()
