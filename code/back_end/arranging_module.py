
class Arranging_module(App):
    categorize_obj = None

    def categorize_obj(map_object):

        #extract google categories from map object

        # helping function, input is google category, output is our category, if doesn't fit to any of our category output should be null
        #it returns list of categories which are related with google category, as it can happen that one google category fit for 2 or more of our categories
        def categorise(googlecategory):  # file path = path to file category.txt
            file_path="categories.txt"
            try:
                with open(file_path, "r") as file:
                    fitting_categories=[]
                    file_contents = file.read()
                    lines = file_contents.strip().split('\n')

                    for line in lines:
                        list = line.split(',')
                        for elem in list:
                            if elem == googlecategory:
                                fitting_categories.append(list[0])

            except FileNotFoundError:
                print(f"File '{file_path}' not found.")
            except IOError:
                print(f"Error reading file '{file_path}'.")
        #map_object[]
    def sort_obj(criterion,m_object_list):
        if (criterion == "rating"):
            pass
        elif (criterion == "distance"):
            pass
        elif (criterion == "name"):
            pass
        elif (criterion == "category"):
            pass
        else:
            return -1

    def start_arranging_module(**m_object_list):
        # -2 for None object
        pass

    def provide_objects():
        pass




#provide_object()







