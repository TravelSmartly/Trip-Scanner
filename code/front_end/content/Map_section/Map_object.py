from kivy.garden.mapview import MapMarkerPopup


class Map_object(MapMarkerPopup):
    cordX: int
    cordY: int
    cord: int
    id: int
    display_status: int
    from_place_list: int

    source = "marker.png"
    market_data = []

    def on_release(self):
        # Open up the LocationPopupMenu
        pass
        # menu = LocationPopupMenu(self.market_data)
        # menu.size_hint = [.8, .9]
        # menu.open()

    def getCord(self): pass
    def getStatus(self): pass

    def setCord(self): pass
    def setStatus(self): pass