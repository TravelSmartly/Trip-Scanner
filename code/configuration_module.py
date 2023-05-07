

class Configuration_module:

	def __init__(self):
		self.profile_name = ''	#blank profile
		self.categories = None	#categories list should be read from the file
		self.interval = 15 #how often to update location, etc in minutes 
		self.proximity = 3 # in kilometers, could be changed in the future
		self.first_timer = False

	def put_profile_to_front (current_profile):
		pass

	def save_profile (current_profile):
		pass

	def save_config_file(profiles, settings, favourites):
		try:
    		with open("config_file.conf", 'w') as fdw:
            	pass #do stuff here  
		except IOError:
    		print "Could not find file: config_file.conf"

	def put_settings_front():
		pass

	

	def read_config_file (name):
		pass

	def start_configuration_module():
		pass
		#Does not return any specific objects, so just make sure that it returns 0 if succeeded
		#Returns -7 if config_file does not exist or could not have been opened