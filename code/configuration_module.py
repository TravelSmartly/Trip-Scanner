
@dataclass
class Configuration_module:
	profile_name: str = '' #blank profile default
	profile_object = '' #json object with profiles
	categories: categories = None #categories list should be read from the file
	interval: int = 15 #how often to update location
	proximity: int = 3 #in kilometers, could be changed in the future
	first_timer: bool = False
	notification_system: bool = True 

	def put_profile_to_front ():
		return self.profile_object
	
	def put_profile_name_front ():
		return self.profile_name

	def save_profile ():
		config_folder_path = pathlib.Path('../config/profiles.json')
		with open(config_folder_path, 'w') as fwd:
			json.dump (self.profile_object, fwd)

	def save_config_file(settings):
    		with open("config_file.conf", 'w') as fdw:
			
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
