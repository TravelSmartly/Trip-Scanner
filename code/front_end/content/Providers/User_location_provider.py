# from back_end.location_module import Location_module





#
# class User_location_provider(unittest.TestCase):
#     def hi(self): print("hi")
#     def setUp(self):
#         # ustawiam recznie pobrane dane
#         self.current_location = (50.06163905474776, 19.936530642326513)
#         # historia lokacji
#         self.location = {}
#
#         # DG: dodałem nową zmienną time, która oznacza czas pobrania w unix
#         self.u_time = 1682657624
#     def test_download_location(self):
#         self.arranging_module = Location_module()
#         self.assertTrue(hasattr(Location_module, 'get_current_location'))
#         # czy pobrane dane są
#         self.assertEqual(self.arranging_module.get_current_location(), self.current_location)
#         self.assertTrue(len(self.current_location), 3)
#         self.u_time = int(time.time())
#         print("HI")
#     def success(self): pass
#     def error(self): pass
#     def failure(self): pass
#
#     def get_location(self): pass
#
#     def set_location(self): pass
#
