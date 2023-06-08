import json

# Otwórz plik json
with open('generalized_categories.json') as f:
    data = json.load(f)



with open('generalized_categories_line.txt', 'a') as f:
    for line in data:
        f.write(f'{line["id"]}, {line["category"]}, {", ".join(line["subcategories"])}\n')
    # f.write(f'{data["ID"]}, {data["Category"]}, {", ".join(data["Subcategories"])}')