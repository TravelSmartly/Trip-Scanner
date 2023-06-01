
class Arranging_module(App):
    categorize_obj = None

    #key_value in dictonary
    #google_category []
    #category []
    def reverse_obs(category_list): #output list of google categories
        #for map_object in map_objects: #toremove
            #google_category = map_object["google_category"]
            #categorise(category_list, map_object)

            # transform category list into fitting google categories

    #def categorise(category_list, map_object):  # file path = path to file category.txt
        file_path = "categories.txt"
        fitting_categories = []
        try:
            with open(file_path, "r") as file:

                file_contents = file.read()
                lines = file_contents.strip().split('\n')
                for line in lines:
                    list = line.split(',')
                    if list[0] in category_list:
                        fitting_categories.extend(list[1:])
                return fitting_categories
                #map_object["category"] = fitting_categories

        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except IOError:
            print(f"Error reading file '{file_path}'.")
        # map_object[]
    def categorize_obj(map_objects):

        # helping function, input is google category, output is our category, if doesn't fit to any of our category output should be null
        # it returns list of categories which are related with google category, as it can happen that one google category fit for 2 or more of our categories
        def categorise(google_category, map_object):  # file path = path to file category.txt
            file_path = "categories.txt"
            fitting_categories = []
            try:
                with open(file_path, "r") as file:

                    file_contents = file.read()
                    lines = file_contents.strip().split('\n')
                    for line in lines:
                        list = line.split(',')
                        for elem in list:
                            if elem == google_category:
                                fitting_categories.append(list[0])
                    map_object["category"] = fitting_categories

            except FileNotFoundError:
                print(f"File '{file_path}' not found.")
            except IOError:
                print(f"Error reading file '{file_path}'.")

        for map_object in map_objects:
            google_category = map_object["google_category"]
            categorise(google_category,map_object)

            #extract google categories from map object


            #map_object[]
    def sort_asc(criterion,map_objects):
        map_objects = sorted(map_objects, key=lambda x: x[criterion]) #ascending_sort

    def sort_desc(criterion,map_objects):
        map_objects = sorted(map_objects, key=lambda x: x[criterion], reverse=True) #descending_sort

    # def start_arranging_module(**m_object_list):
    #     # -2 for None object
    #
    #     pass

    # def provide_objects():
    #     pass




#provide_object()







