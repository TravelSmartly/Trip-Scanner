
@dataclass
class Configuration_module:
	profile_current: str = '' #blank profile default
	profiles_object = '' #json object with profiles
	interval: int = 15 #how often to update location
	proximity: int = 3 #in kilometers, could be changed in the future
	first_timer: bool = False
	notification_system: bool = True 
	night_mode: bool = False

	def put_profiles_to_front ():
		return self.profile_object
	
	def put_profile_name_front ():
		return self.profile_current

	def set_current_profile (current_profile_object):
		self.profile_current = current_profile_object

	def save_profiles ():
		config_folder_path = pathlib.Path('../config/profiles.json')
		with open(config_folder_path, 'w') as fwd:
			json.dump (self.profile_object, fwd)

	def read_profiles ():
		config_folder_path = pathlib.Path('../config/profiles.json')
		with open(config_folder_path) as frd:
			self.profile_object = json.loads(frd.read())

	def save_config_file(settings):
		config_folder_path = pathlib.Path('../config/config_file.cfg')
    	with open("config_file.conf", 'w') as fwd:
			fwd.write (self.first_timer + '\n' +
			self.notification_system + '\n' + 
			self.interval + '\n' +
			self.night_mode + '\n' +
			self.profile_current + '\n')
	
	def read_config_file (name):
		config_folder_path = pathlib.Path('../config/config_file.cfg')
    	with open("config_file.conf") as frd:
			conf = list(frd.read().split('\n'))
			self.notification_system, self.interval, self.night_mode, self.profile_current = *conf
			

	def put_settings_front():
		pass

	

	

	def start_configuration_module():
		pass
		#Does not return any specific objects, so just make sure that it returns 0 if succeeded
		#Returns -7 if config_file does not exist or could not have been opened
