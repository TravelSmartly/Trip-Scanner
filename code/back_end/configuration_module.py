from dataclasses import dataclass
import json
import pathlib
import os

@dataclass
class Configuration_module:
	profile_current = [] #blank profile default
	profiles_object = [] #json object with profiles
	categories_object = [] #json object with categories
	interval: int = 15 #how often to update location
	proximity: int = 3 #in kilometers, could be changed in the future
	first_timer: bool = True
	notification_system: bool = True 
	night_mode: bool = False

	def hi(self):
		print("HI IT IS Configuration_module")

	## Uwaga, tutaj zwracam i bede operowac na profilu bezposrednio pobranego z back-endu,
	## wszystkie zmiany we front-endzie, czy gdize kolwiek takze od razu beda pojawialy sie w tym obiekcie
	def put_profiles_to_front (self):
		return self.profile_object

	def put_categories_to_front (self):
		return self.categories_object

	def put_selected_profile_to_front (self):
		return self.profile_current

	def get_interval (self):
		return self.interval

	def update_interval (self, interv):
		self.interval = interv

	## RemXYZ: pobieram wszystkie profile, dalej za pomoca petli szukam ten, ktory ma w selected 1, i przyrownuje go do zmiennej profile_current, zatrzymujac przy tym petle i zwracam 0
	def find_current_profile(self):
		profiles = self.put_profiles_to_front()
		for profile in profiles:
			if profile["selected"] == 1:
				# print(profile)
				self.profile_current = profile
				return 0
		return -1

	def set_current_profile (self, current_profile_object):
		self.profile_current = current_profile_object

	def save_profiles (self, profiles = None) -> int:
		if profiles is None:
			profiles = self.profile_object
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
				## RemXYZ: Uwaga, kiedy odtzytujemy json plik, to pierwszy dotajemy element "profiles"
				## i wlasnie ten element "profiles" zawiera w sobie wszystkie profile,
				##  wiec musze go pobrac na samym poczatku
				## czyli to wyglada tak {"profiles": {name:"profile0", selected:1,...} ...}
				self.profile_object = profiles
				return 0
				# print(self.profile_object)
		## RemXYZ: Dodałem Try exept, zeby na wszelki wypadek aplikacja sie nie zamknela
		except Exception as e:
			self.profile_object = []
			return -1


	def read_categories(self) -> int:
		#categories_file_path = "categories/generalized_categories.json"
		config_folder_path = pathlib.Path.cwd() / 'config' / 'generalized_categories.json'
		#print(config_folder_path)
		try:
			with open(config_folder_path) as frd:
				self.categories_object = json.load(frd)
				return 0
		except Exception as e:
			self.categories_object = []
			return -1


	def save_config_file(self,settings = None):
		config_folder_path = pathlib.Path.cwd() / 'config' / 'config_file.cfg'
		with open(config_folder_path, 'w') as fwd:
			fwd.write (self.first_timer + '\n' +
			self.notification_system + '\n' +
			self.interval + '\n' +
			self.night_mode + '\n' +
			self.profile_current + '\n')
			return 0
		return -1

	def read_config_file (self):
		config_folder_path = pathlib.Path.cwd() / 'config' / 'config_file.cfg'
		if not config_folder_path.is_file():
			return -1
		with open(config_folder_path) as frd:
			conf = list(frd.read().split('\n'))
			self.notification_system, self.interval, self.night_mode, self.profile_current = conf
		return 0
			
	### During first app usage, this method creates 
	### all needed configuration files 
	def create_config_file (self):
		self.first_timer = False
		working_dir_path = pathlib.Path.cwd() / 'config'
		if not working_dir_path.is_dir():
			working_dir_path.mkdir()
		config_folder_path = working_dir_path / 'config_file.cfg'
		if config_folder_path.is_file():
			return -1
		with open(config_folder_path, 'a') as fwd:
			fwd.write (self.first_timer + '\n' +
			self.notification_system + '\n' +
			self.interval + '\n' +
			self.night_mode + '\n' +
			self.profile_current + '\n')
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
