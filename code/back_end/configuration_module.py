from dataclasses import dataclass
import json
import pathlib
import os

@dataclass
class Configuration_module:
	profile_current = {} #blank profile default
	profiles_object = [] #json object with profiles
	categories_object = None #json object with categories
	categories_dicts = [] #list of dicts with categories
	interval: int = 15 #how often to resend notifications
	proximity: int = 500 #in meters, could be changed in the future
	notification_system: int = 1 
	night_mode: int = 0

	def hi(self):
		print("HI IT IS Configuration_module")

	## Uwaga, tutaj zwracam i bede operowac na profilu bezposrednio pobranego z back-endu,
	## wszystkie zmiany we front-endzie, czy gdize kolwiek takze od razu beda pojawialy sie w tym obiekcie
	def put_profiles_to_front (self):
		return self.profiles_object

	def put_categories_to_front (self):
		return self.categories_object

	def put_selected_profile_to_front (self):
		return self.profile_current

	def get_interval (self):
		return int(self.interval)

	def update_interval (self, interv):
		self.interval = interv

	### from json object kept in config object type, this function
	### finds and set currently selected by user profile
	### returns 0 on sucess, otherwise -1 if selected profile wasnt found
	### that usually implies something went wrong earlier, for example
	### while reading config files
	def find_current_profile(self):
		profiles = self.profiles_object
		#profiles = json.loads (self.put_profiles_to_front())
		for profile in profiles:
			if profile["selected"] == 1:
				self.profile_current = profile
				return 0
		return -1

	def set_current_profile (self, current_profile_object):
		self.profile_current = current_profile_object

	### saves all json profile object to the memory
	### returns 0 on success, otherwise -1
	def save_profiles (self, profiles = None) -> int:
		if profiles is None:
			profiles = self.profiles_object
		config_folder_path = pathlib.Path.cwd() / 'config' / 'profiles.json'
		try:
			with open(config_folder_path, 'w') as fwd:
				json.dump(profiles, fwd)
				return 0
		except Exception as e:
			return -1

	### Read json file with all available profiles created by users
	### returns 0 on sucess, otherwise -1
	def read_profiles (self) -> int:
		config_folder_path = pathlib.Path.cwd() / 'config' / 'profiles.json'
		try:
			with open(config_folder_path) as frd:
				profiles = json.loads(frd.read())
				self.profiles_object = profiles
				print (type(profiles))
				for profile in profiles:
					if profile['selected'] == 1:
						print ("found:", profile)
						self.profile_current = profile
						print (self.put_selected_profile_to_front())
						print (self.put_profiles_to_front())
				return 0
				# print(self.profile_object)
		except Exception as e:
			self.profiles_object = []
			return -1


	### method to read json file with all available categories
	### categories could be extended in the future and packed to this file
	### on sucess, method returns 0, otherwise -1
	def read_categories(self) -> int:
		config_folder_path = pathlib.Path.cwd() / 'config' / 'generalized_categories.json'
		try:
			with open(config_folder_path) as frd:
				self.categories_object = json.load(frd)
				return 0
		except Exception as e:
			self.categories_object = []
			return -1
	
	### this method is a counterpart of simple read_categories method
	### both should contain the same list with categories, the difference
	### is just with format -> if for some reason using simple txt file
	### with each category as line would be more convinient
	### this method would be used
	def read_categories_txt (self) -> int:
		config_folder_path = pathlib.Path.cwd() / 'config' / 'generalized_categories_lines.txt'
		with open (config_folder_path) as frd:
			txt_file = frd.readlines()
			for line in txt_file:
				s_line = line.strip().split(', ')
				ide = int(s_line[0])
				category = s_line[1]
				subcategories = [s_line[i] for i in range(2,len(s_line))]
				category_dict = {"id": ide, "category": category, "subcategories": subcategories}
				self.categories_dicts.append (category_dict)
			return 0
		return -1

	def get_categories_dicts (self):
		return self.categories_dicts

	### saving config file on the disk should be done with this method
	### from all other classes and positions
	## returns 0 if opening and saving to the file was successful
	def save_config_file(self,settings = None):
		config_folder_path = pathlib.Path.cwd() / 'config' / 'config_file.cfg'
		with open(config_folder_path, 'w') as fwd:
			fwd.write (f"{self.interval} \n{self.proximity} \n{self.notification_system} \n{self.night_mode}")
			return 0
		return -1

	### reading file method, returns 0 if read was sucessful
	### be careful with types when using this method, as python often keeps
	### data as a string where it can, especially with building on android
	### that caused some bugs in the past
	def read_config_file (self):
		config_folder_path = pathlib.Path.cwd() / 'config' / 'config_file.cfg'
		if not config_folder_path.is_file():
			return -1
		with open(config_folder_path) as frd:
			conf = list(frd.read().split('\n'))
			self.interval = int(conf[0])
			self.proximity = int(conf[1])
			self.notification_system = int(conf[2])
			self.night_mode = int(conf[3])
		return 0
			
	### During first app usage, this method creates 
	### all needed configuration files 
	### returns -1 if config file exists, which should be default behavior
	### as this file should be provided with package built for android
	def create_config_file (self):
		working_dir_path = pathlib.Path.cwd() / 'config'
		if not working_dir_path.is_dir():
			working_dir_path.mkdir()
		config_folder_path = working_dir_path / 'config_file.cfg'
		if config_folder_path.is_file():
			return -1
		with open(config_folder_path, 'a') as fwd:
			fwd.write (f"{self.interval} \n{self.proximity} \n{self.notification_system} \n{self.night_mode}")
		profiles_path, gen_cat_path = working_dir_path / 'profiles.json', working_dir_path / 'generalized_categories.json'
		profiles_path.touch()
		gen_cat_path.touch()
		return 0

		
	def put_settings_front(self):
		pass

	

	

	def start_configuration_module(self):
		pass
		#Does not return any specific objects, so just make sure that it returns 0 if succeeded
		#Returns -7 if config_file does not exist or could not have been opened
		
		#notification options: normal and more subtle
		#day or night mode
		#font size, normal and eye-friendly
		#remember about colors - recognisable to colorblind-people
		#button for feedback
		
		### for next versions
		# auto translation by google translator for exmaple
		# text to speech, no need to look at phone each time
		# 
