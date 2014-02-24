import os
import random 
import subprocess
 


class Sound() :

	def play_from_dir(self, folderName):


		baseDir = os.path.dirname(os.path.realpath(__file__)) + "/sounds/" + folderName	
		audio = baseDir + "/" + random.choice(os.listdir(baseDir)) 
		subprocess.call(["mplayer",audio])
