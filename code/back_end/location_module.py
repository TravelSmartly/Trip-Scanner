## RemXYZ: Bez tego nie dziala
# from classmethod import classmethod
import math

### default location changed to Krakow
class Location_module:
    lat = 111045 #one degree of latitude is always 69 miles = 111045 meters
    lon = 111045 #one degree of latitude in equator, sea level is 69 miles = 111045 meters
    center_location = (50.05918219735402, 20.003032346862184) #last saved location of a user, center of an ellipse
    current_location = (50.05918219735402, 20.003032346862184) 

    @classmethod
    def on_gps_location(cls, *args, **kwargs)->None:
        cls.current_location = tuple((kwargs["lat"], kwargs["lon"]))

    @classmethod
    def on_auth_status (cls, general_status, status_message):
        if general_status == 'provider-enabled':
            pass
        else:
            print ('gps serror')

    ### This method should return a tuple 
    ### with current user coordinates
    @classmethod
    def get_current_location(cls):
        # cls.current_location[0] =  cls.current_location[0] + 0.1
        # cls.current_location[1] += cls.current_location[1] + 0.1
        try:
            return cls.current_location
        except Exception as e:
            return -1

    ### This method should return true if current_location
    ### is inside an elipse with the center in center_location variable
    @classmethod
    def check_proximity(cls,r,current_location,center_location)->bool:
        return pow((cls.current_location[0]-cls.center_location[0]) * cls.lat, 2) + pow((cls.current_location[1] - cls.center_location[1]) * cls.lon * math.cos((cls.current_location[0] + cls.center_location[0])/2), 2) < pow(r,2)


    ### Method that allows to get user current location
    ### to front
    @classmethod
    def put_user_location_front(cls):
        tmp = cls.get_current_location()
        if tmp == (-1, -1):
            print("gps not working")
        tmp = tuple (map(float, tmp))
        return tmp

    #@classmethod
    #def start_location_module(cls, r, center_location):
        #current_location = cls.get_current_location()
        #searcher = None
        #if not (cls.check_proximity(r,current_location,center_location)):#is outside of region
            #center_location = current_location
            #odpal searching module
            #cls.center_location = current_location
            #searcher = Searching_module(current_location)
            #try:
              # searcher.start_searching_module(current_location)
              # return searcher
           # except TypeError:
           #     print("Searcher for some reason didn't get initialised properly...")
          #      return -2
        #return 0



