import os
from mplayer import Player

player = Player()
abspath = os.path.join(os.path.dirname(__file__), 'desafio21/song.m4a')
player.loadfile(abspath)