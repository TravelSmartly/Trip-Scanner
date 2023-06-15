# Class Arranging_module:

    reverse_obs(category_list): This method takes a category_list as input and is intended to be used to reverse-observe map objects. However, the implementation is incomplete, as the actual functionality is commented out. It seems that the goal is to transform the category list into fitting Google categories, but the code inside the method is currently missing.

    categorize_obj(map_objects): This method categorizes map objects based on their Google category. It iterates over the map_objects list and calls the categorise function for each map object. The categorise function reads a file called "categories.txt" and assigns fitting categories to the map object based on its Google category.

    sort_asc(criterion, map_objects): This method sorts the map_objects list in ascending order based on the provided criterion. It uses the sorted function and a lambda function as the key to specify the criterion for sorting.

    sort_desc(criterion, map_objects): This method sorts the map_objects list in descending order based on the provided criterion. It uses the sorted function, similar to the sort_asc method, but with the reverse parameter set to True.

	

# Class Configuration_module: 
Represents a configuration module and contains various methods related to handling profiles, categories, and configuration settings. Here is an overview of the methods and attributes in the class:

### Attributes:

    profile_current: A dictionary representing the current profile.
    profiles_object: A list containing JSON objects representing profiles.
    categories_object: A JSON object containing categories.
    categories_dicts: A list of dictionaries with category information.
    interval: An integer representing the interval value.
    proximity: An integer representing the proximity value.
    notification_system: An integer representing the notification system.
    night_mode: An integer representing the night mode setting.

### Methods:

    hi(): Prints a simple message to indicate that the configuration module is active.
    put_profiles_to_front(): Returns the profiles_object attribute.
    put_categories_to_front(): Returns the categories_object attribute.
    put_selected_profile_to_front(): Returns the profile_current attribute.
    get_interval(): Returns the interval attribute as an integer.
    update_interval(interv): Updates the interval attribute with the provided interv value.
    find_current_profile(): Searches for the currently selected profile in the profiles_object list and updates the profile_current attribute accordingly. Returns 0 if successful or -1 if no current profile is found.
    set_current_profile(current_profile_object): Updates the profile_current attribute with the provided current_profile_object.
    save_profiles(profiles): Saves the provided profiles (or profiles_object if not provided) to a JSON file.
    read_profiles(): Reads and loads the profile data from a JSON file into the profiles_object attribute. Returns 0 on success or -1 if an error occurs.
    read_categories(): Reads and loads the category data from a JSON file into the categories_object attribute. Returns 0 on success or -1 if an error occurs.
    read_categories_txt(): Reads and parses category data from a text file into the categories_dicts attribute. Returns 0 on success or -1 if an error occurs.
    get_categories_dicts(): Returns the categories_dicts attribute.
    save_config_file(settings): Saves the provided settings (or configuration attribute values) to a config file.
    read_config_file(): Reads and loads the configuration values from a config file into the corresponding attributes. Returns 0 on success or -1 if the config file does not exist or cannot be opened.
    create_config_file(): Creates the necessary configuration files for the application. Returns 0 on success or -1 if the files already exist.
    put_settings_front(): Not implemented.
	
	

	
	
	
	
# Class Location_module: 
Represents a location module and contains methods and attributes related to handling user locations. Here is an overview of the class:

### Attributes:

    lat: A constant representing the value of one degree of latitude in meters.
    lon: A constant representing the value of one degree of longitude in meters.
    center_location: A tuple representing the last saved location of the user, considered as the center of an ellipse.
    current_location: A tuple representing the current location of the user.

### Methods:

    on_gps_location(*args, **kwargs): A class method that updates the current_location attribute based on the provided latitude (lat) and longitude (lon) values.
    on_auth_status(general_status, status_message): A class method that handles the GPS authorization status. If the general status is "provider-enabled," the method does nothing. Otherwise, it prints "gps error."
    get_current_location(): A class method that returns the current location as a tuple. If the current location is not available, it returns -1.
    check_proximity(r, current_location, center_location): A class method that checks whether the current_location is inside an ellipse with the center_location as the center. It returns True if the current location is inside the ellipse, and False otherwise.
    put_user_location_front(): A class method that retrieves the user's current location and returns it as a tuple. If the current location is not available, it prints "gps not working" and returns (-1, -1).
	
	
	

	
	
	

	
	
# Class Searching_module: 
Represents a searching module and contains methods and attributes related to searching for places in a given area. Here is an overview of the class:

### Attributes:

    API_KEY: A string representing the API key used for accessing the search API.
    config_module: A reference to the configuration module.

### Methods:

    __init__(self, current_location=None): The constructor method for the Searching_module class. It initializes the m_object_list attribute as an empty list.
    set_config_module(self, config_module): Sets the config_module attribute of the searching module to the provided config_module.
    convert_miles_to_meters(self, miles): Converts a distance in miles to meters. Returns the converted value or -1 if an error occurs.
    distance_between_two_latlon(self, lat_lon1, lat_lon2): Calculates the distance between two sets of latitude and longitude coordinates using the Haversine formula. Returns the distance in meters or -1 if an error occurs.
    get_m_object_list(self): Returns the m_object_list attribute, which contains the list of search results.
    set_m_object_list(self, my_list): Sets the m_object_list attribute to the provided list.
    remove_old_objects(self): Clears the m_object_list attribute.
    search_the_area(self, coordinates, radius, category, subcategory): Searches for places in the specified area based on the provided coordinates, radius, category, and subcategory. It uses the Overpass API to retrieve place data. The search results are stored in the m_object_list attribute.
    get_search_result(self): Retrieves the search results based on the selected categories from the configuration module. It clears the m_object_list attribute, performs the search for each selected category and subcategory, and returns the updated m_object_list.
	
	
