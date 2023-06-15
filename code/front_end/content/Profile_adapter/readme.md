# Class Profile_adapter:

    Inherits from Profile_provider and processes data in a format that is more useful for other parts of the system.
    __init__(self, conf_module: object): The constructor method for the Profile_adapter class. It calls the constructor of the parent class.
    hi(self): A method that prints "hi profile adapter".
    postprocessing(self): Downloads the profiles, processes them, and stores them in the profiles attribute. It also downloads the selected profile and stores it in the selected attribute.
    download_selected_profile(self): Downloads the selected profile from the backend.
    get_instraction(self): Returns the instruction dictionary for reading profiles.
    get_selected(self): Returns the selected profile.
    get_profiles(self): Returns the processed profiles.
    set_profiles_instraction(self, pro_inst): Sets the instruction dictionary for reading profiles.
    set_location_data(self): Sets the location data.
	
	
	
	
# Class Profile_manipulator:

    Inherits from Profile_adapter and extends its functionality by adding methods to manipulate profiles.
    __init__(self, conf_module: object): The constructor method for the Profile_manipulator class. It calls the constructor of the parent class.
    select_category(self, id: int) -> int: Selects a category by adding its ID to the selected categories list. It also handles the logic for category changes and updates the is_categories_changed attribute.
    set_default_selector(self): Resets the category selection to its default state.
    deselect_category(self, id: int) -> int: Deselects a category by removing its ID from the selected categories list. It also handles the logic for category changes and updates the is_categories_changed attribute.
    prepare_send_profile(self) -> int: Prepares the profile data to be sent to the backend.
    get_selected_categories(self): Returns the selected categories.
    get_change_status(self): Returns whether any changes have been made to the categories.
	

# Class Category_adapter:

    Inherits from Profile_provider and adapts category data to the format used in other parts of the system.
    __init__(self, conf_module: object): The constructor method for the Category_adapter class. It calls the constructor of the parent class.
    hi(self): A method that prints "hi categories adapter".
    postprocessing(self) -> int: Downloads the categories, processes them, and stores them in the categories attribute.
    get_categories(self) -> list: Returns the processed categories.
    get_instraction(self) -> dict: Returns the instruction dictionary for reading categories.
    set_instraction(self, cat_inst: dict): Sets the instruction dictionary for reading categories.
    set_categories(self): Sets the categories.
