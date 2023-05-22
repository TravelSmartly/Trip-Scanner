from kivy.app import App
from kivy.uix.label import Label
from plyer import gps

class Location_module:
    lat = 111045 #one degree of latitude is always 69 miles = 111045 meters
	lon = 111045 #one degree of latitude in equator, sea level is 69 miles = 111045 meters
	center_location: tuple[float, float] #last saved location of a user
	current_location: tuple[float, float] 
    #s_string:str
    #type hints

    def __init__():
        test = 0

    @classmethod
    def on_gps_location(cls, *args, **kwargs)->None:
        #kwargs["lat"]=10.0
        #kwargs["lon"]=10.0
        #print(kwargs)
        cls.current_location = tuple((kwargs["lat"], kwargs["lon"])) 

    @classmethod
    def get_current_location(cls)->int:
        try:
            gps.configure(on_location=cls.on_gps_location)
            gps.start()
            time.sleep(1)
            gps.stop()
            #coordinates = gps.
            return cls.current_location
        except Exception as e:
            return -1

    @classmethod
    def check_proximity(cls,r,current_location,center_location)->bool:
        #zwraca true jesli current_location jest w srodku elipsy o srodku w punkcie center_location
        return (cls.current_location[0]-cls.center_location[0] * cls.lat) ^ 2 + (cls.current_location[1] - cls.center_location[1] * cls.lon * math.cos((cls.current_location[0] + cls.center_location[0])/2))^2 < (r)^2





    @classmethod
    def put_user_location_front(cls):
        tmp = cls.get_current_location()
        if tmp == -1:
            print("gps not working")
        return tmp
        #give coordinated for current or center location

    @classmethod
    def start_location_module(cls, r, center_location):
        current_location = cls.get_current_location()
        searcher = None
        if not (cls.check_proximity(r,current_location,center_location)):#is outside of region
            #center_location = current_location
            #odpal searching module
            cls.center_location = current_location
            searcher = searching_module.Searching_module(current_location)
            try:
               searcher.start_seaching_module()
               return searcher
            except TypeError:
                print("Searcher for some reason didn't get initialised properly...")
                return -2
        return 0



