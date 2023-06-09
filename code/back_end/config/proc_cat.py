src = "generalized_categories_line.txt"
file = None
with open(src, "r") as f:
     file = f.readlines()

for line in file:
     s_line = line.strip().split(", ")
     id = s_line[0]
     category = s_line[1]
     subcategories = [s_line[i] for i in range(2,len(s_line))]
     print(id, category, subcategories)


src = "generalized_categories_line.txt"
file = None
with open(src, "r") as f:
     file = f.readlines()

for line in file:
     s_line = line.strip().split(", ")
     id = s_line[0]
     category = s_line[1]
     subcategories = [s_line[i] for i in range(2,len(s_line))]
     print(id, category, subcategories)
