import os
#first step: rearrange text file:
# with open("google_categories_raw.txt", "r") as input_file, open("google_categories.txt", "w") as output_file:
#     for line in input_file:
#         modified_line = line.replace(" \t", "\n")
#         output_file.write(modified_line)
#
#       input_file.close()
#       output_file.close()
#     #os.remove("google_categories_raw.txt")
#     #os.rename('a.txt', 'b.kml')

#second step: assemble for first time

key_words = ['Karate']#Car,Tire #clinic#bar, pub#shop#
category = ["Restaurant"]#motorization #medical#bar#shops#
# keep evaluating and then switching these list for each iteration

with open('google_categories.txt') as input_file, open('google_categories_new.txt', 'w') as output_file:
    for line in input_file:
        if not any(key_word in line for key_word in key_words):
            output_file.write(line)
        else:
            category.append(line)
    input_file.close()
    output_file.close()
    os.remove("google_categories.txt")
    os.rename('google_categories_new.txt', 'google_categories.txt')


with open("categories.txt", "w") as fp:
    fp.write(",".join(str(item) for item in category))
print("Done")


