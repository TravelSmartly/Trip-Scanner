# import json
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
# from nltk.metrics.distance import edit_distance
# nltk.download('stopwords')
#
# def preprocess_text(text):
#     # Tokenizacja tekstu
#     tokens = word_tokenize(text.lower())
#
#     # Usunięcie stopwords
#     stop_words = set(stopwords.words('english'))
#     tokens = [token for token in tokens if token not in stop_words]
#
#     # Lemmatyzacja tokenów
#     lemmatizer = WordNetLemmatizer()
#     tokens = [lemmatizer.lemmatize(token) for token in tokens]
#
#     return tokens
#
# def calculate_similarity(token1, token2):
#     # Obliczenie podobieństwa między dwoma tokenami na podstawie dystansu edycyjnego
#     return edit_distance(token1, token2)
#
#
# # Lista miejsc
# places = [
#     "Abbey",
#     "Fencing Salon",
#     "Parochial School",
#     "Aboriginal and Torres Strait Islander Organisation",
#     "Fencing School",
#     "Parsi Temple",
#     "Aboriginal Art Gallery",
#     "Feng Shui Consultant",
#     "Part Time Daycare",
#     "Abortion Clinic",
#     "Feng Shui Shop",
#     "Party Equipment Rental Service",
#     "Abrasives Supplier",
#     "Ferris wheel",
#     "Party Planner",
#     "Abundant Life Church",
#     "Ferry Service",
#     "Party Store",
#     "Accountant",
#     "Fertility Clinic",
#     "Passport Agent",
#     "Accounting Firm"
# ]
#
# # Uogólnione kategorie
# categories = {
#     "Category1": [],
#     "Category2": [],
#     "Category3": [],
#     "Category4": [],
#     "Category5": []
#     # Dodaj pozostałe kategorie
# }
#
# # Przetwarzanie i kategoryzacja miejsc
# for place in places:
#     # Przetwarzanie tekstu
#     tokens = preprocess_text(place)
#
#     # Znalezienie najbardziej podobnej kategorii
#     min_similarity = float('inf')
#     matching_category = None
#
#     for category, category_tokens in categories.items():
#         similarity = sum(
#             [calculate_similarity(token, category_token) for token in tokens for category_token in category_tokens])
#
#         if similarity < min_similarity:
#             min_similarity = similarity
#             matching_category = category
#
#     # Dodanie miejsca do odpowiadającej kategorii
#     categories[matching_category].append(place)
#
# # Zapisanie kategorii do pliku JSON
# with open('categories.json', 'w') as file:
#     json.dump(categories, file)




# import json
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
# from nltk.metrics.distance import edit_distance
#
# # Przykładowa lista miejsc
# places = [
#     "Abbey",
#     "Fencing Salon",
#     "Parochial School",
#     "Aboriginal and Torres Strait Islander Organisation",
#     "Fencing School",
#     "Parsi Temple",
#     "Aboriginal Art Gallery",
#     "Feng Shui Consultant",
#     "Part Time Daycare",
#     "Abortion Clinic",
#     "Feng Shui Shop",
#     "Party Equipment Rental Service",
#     # Dodaj więcej miejsc
# ]
#
# # Uogólnione kategorie
# categories = {}
#
# # Przetwarzanie i kategoryzacja miejsc
# for place in places:
#     # Przetwarzanie tekstu
#     tokens = word_tokenize(place.lower())
#     stop_words = set(stopwords.words('english'))
#     tokens = [token for token in tokens if token not in stop_words]
#     lemmatizer = WordNetLemmatizer()
#     tokens = [lemmatizer.lemmatize(token) for token in tokens]
#
#     # Wyszukiwanie najbardziej podobnej kategorii
#     min_similarity = float('inf')
#     matching_category = None
#
#     for category, category_tokens in categories.items():
#         similarity = sum([edit_distance(token, category_token) for token in tokens for category_token in category_tokens])
#
#         if similarity < min_similarity:
#             min_similarity = similarity
#             matching_category = category
#
#     # Dodawanie miejsca do odpowiadającej kategorii
#     if matching_category is None:
#         # Tworzenie nowej kategorii, jeśli nie ma pasującej
#         new_category = f"Category{len(categories) + 1}"
#         categories[new_category] = [place]
#     else:
#         # Dodawanie miejsca do istniejącej kategorii
#         categories[matching_category].append(place)
#
# # Generowanie nazw uogólnionych kategorii
# generalized_categories.json = {}
#
# for category, places in categories.items():
#     # Tworzenie nazwy uogólnionej kategorii
#     name_parts = []
#     for place in places:
#         name_parts.extend(word_tokenize(place.lower()))
#
#     name_parts = [lemmatizer.lemmatize(part) for part in name_parts if part not in stop_words]
#     category_name = ' '.join(name_parts)
#
#     # Dodawanie nazwy uogólnionej kategorii do słownika
#     generalized_categories.json[category] = category_name
#
# # Zapisywanie kategorii i nazw uogólnionych do pliku JSON
# output_data = {
#     "categories": categories,
#     "generalized_categories.json": generalized_categories.json
# }
#
# with open('categories.json', 'w') as file:
#     json.dump(output_data, file)











#
# from nltk.corpus import wordnet as wn
# import json
#
# # Lista miejsc
# places = [
#     "Abbey",
#     "Fencing Salon",
#     "Parochial School",
#     "Aboriginal and Torres Strait Islander Organisation",
#     "Fencing School",
#     "Parsi Temple",
#     "Aboriginal Art Gallery",
#     "Feng Shui Consultant",
#     "Part Time Daycare",
#     "Abortion Clinic",
#     "Feng Shui Shop",
#     "Party Equipment Rental Service",
#     "Abrasives Supplier",
#     "Ferris wheel",
#     "Party Planner",
#     "Abundant Life Church",
#     "Ferry Service",
#     "Party Store",
#     # reszta miejsc
# ]
#
# # Tworzenie słownika kategorii
# categories = {}
#
# # Przetwarzanie każdego miejsca
# for place in places:
#     synsets = wn.synsets(place)
#
#     # Jeżeli znaleziono synsety dla miejsca
#     if synsets:
#         synset = synsets[0]  # Wybór pierwszego synsetu
#         hypernym_paths = synset.hypernym_paths()
#
#         # Pobieranie hiperonimu dla ścieżek hiperonimicznych
#         for path in hypernym_paths:
#             for i, synset in enumerate(path):
#                 # Pobieranie nazwy hiperonimu
#                 hypernym_name = synset.lemmas()[0].name()
#
#                 # Tworzenie kategorii, jeżeli jeszcze nie istnieje
#                 if hypernym_name not in categories:
#                     categories[hypernym_name] = []
#
#                 # Dodawanie miejsca do odpowiedniej kategorii
#                 if i == len(path) - 1:
#                     categories[hypernym_name].append(place)
#
# # Utworzenie ostatecznej listy kategorii
# final_categories = [{"Kategoria": kategoria, "Podkategorie": miejsca} for kategoria, miejsca in categories.items()]
#
# # Zapisanie listy kategorii do pliku JSON
# with open("kategorie.json", "w") as file:
#     json.dump(final_categories, file, indent=4)
#
#
# import json
# from nltk.corpus import wordnet
#
# categories = [
#     "Abbey",
#     "Fencing Salon",
#     "Parochial School",
#     "Aboriginal and Torres Strait Islander Organisation",
#     "Fencing School",
#     "Parsi Temple",
#     "Aboriginal Art Gallery",
#     "Feng Shui Consultant",
#     "Part Time Daycare",
#     "Abortion Clinic",
#     "Feng Shui Shop",
#     "Party Equipment Rental Service",
#     "Abrasives Supplier",
#     "Ferris wheel",
#     "Party Planner",
#     "Abundant Life Church",
#     "Ferry Service",
#     "Party Store",
#     # Pozostałe kategorie...
# ]
#
# # Tworzenie słownika dla kategorii
# categories_dict = {}
#
# # Iteracja po kategoriach
# for category in categories:
#     # Pobranie synsetów (grup znaczeniowych) dla danej kategorii
#     synsets = wordnet.synsets(category)
#
#     # Sprawdzenie, czy dla kategorii istnieje synset
#     if synsets:
#         found_hypernym = False
#         # Przeszukiwanie synsetów w poszukiwaniu hiperonimów
#         for synset in synsets:
#             hypernyms = synset.hypernyms()
#             if hypernyms:
#                 # Pobranie nazwy hiperonimu
#                 hypernym_name = hypernyms[0].lemmas()[0].name().replace("_", " ")
#                 # Dodanie kategorii do odpowiedniej uogólnionej kategorii w słowniku
#                 if hypernym_name not in categories_dict:
#                     categories_dict[hypernym_name] = []
#                 categories_dict[hypernym_name].append(category)
#                 found_hypernym = True
#                 break
#
#         # Jeśli nie znaleziono hiperonimu, użyj oryginalnej kategorii jako uogólnionej kategorii
#         if not found_hypernym:
#             if category not in categories_dict:
#                 categories_dict[category] = []
#             categories_dict[category].append(category)
#     else:
#         # Jeśli nie znaleziono synsetu, użyj oryginalnej kategorii jako uogólnionej kategorii
#         if category not in categories_dict:
#             categories_dict[category] = []
#         categories_dict[category].append(category)
#
# # Konwersja słownika na format JSON
# result = {"Kategorie": []}
# for hypernym_name, subcategories in categories_dict.items():
#     result["Kategorie"].append({
#         "Kategoria": hypernym_name,
#         "Podkategorie": subcategories
#     })
#
# # Zapisanie wyniku do pliku JSON
# with open("uogolnione_kategorie.json", "w") as json_file:
#     json.dump(result, json_file, indent=4)


import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus import brown
from nltk.cluster.util import cosine_distance
from nltk.cluster import KMeansClusterer
import numpy as np

def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wn.ADJ, "N": wn.NOUN, "V": wn.VERB, "R": wn.ADV}
    return tag_dict.get(tag, wn.NOUN)

def get_category_tokens():
    """Get tokens from category list"""
    tokens = []
    for category in category_list:
        tokens.extend(category.lower().split())
    return tokens

def get_category_vectors(tokens):
    """Get word vectors for category tokens"""
    category_vectors = []
    for token in tokens:
        synsets = wn.synsets(token, pos=get_wordnet_pos(token))
        if synsets:
            vector = synsets[0].lemmas()[0].name()
            category_vectors.append(vector)
    return category_vectors

def calculate_similarity_matrix(vectors):
    """Calculate similarity matrix for word vectors"""
    similarity_matrix = np.zeros((len(vectors), len(vectors)))
    for i in range(len(vectors)):
        for j in range(len(vectors)):
            if i != j:
                similarity_matrix[i][j] = 1 - cosine_distance(vectors[i], vectors[j])
    return similarity_matrix

def cluster_categories(similarity_matrix):
    """Cluster categories based on similarity matrix"""
    clusterer = KMeansClusterer(num_clusters, distance=nltk.cluster.util.cosine_distance, repeats=25)
    assigned_clusters = clusterer.cluster(similarity_matrix, assign_clusters=True)
    return assigned_clusters

def generalize_categories(cluster_assignments):
    """Generalize categories based on cluster assignments"""
    category_clusters = {}
    for i in range(len(cluster_assignments)):
        cluster = cluster_assignments[i]
        category = category_list[i]
        if cluster in category_clusters:
            category_clusters[cluster].append(category)
        else:
            category_clusters[cluster] = [category]
    return category_clusters

def print_generalized_categories(category_clusters):
    """Print generalized categories"""
    for cluster, categories in category_clusters.items():
        print("Cluster", cluster)
        print("--------------------")
        for category in categories:
            print(category)
        print("\n")

# List of categories
category_list = [
    "Abbey", "Fencing Salon", "Parochial School", "Aboriginal and Torres Strait Islander Organisation",
    "Fencing School", "Parsi Temple", "Aboriginal Art Gallery", "Feng Shui Consultant",
    "Part Time Daycare", "Abortion Clinic", "Feng Shui Shop", "Party Equipment Rental Service",
    "Abrasives Supplier", "Ferris wheel", "Party Planner", "Abundant Life Church", "Ferry Service",
    "Party Store", "Accountant", "Fertility Clinic", "Passport Agent", "Accounting Firm",
    "Fertility Physician", "Passport Office", "Accounting School", "Fertilizer Supplier",
    "Passport Photo Processor", "Accounting Software Company", "Festival", "Pasta Shop",
    "Acoustical Consultant", "Festival Hall", "Pastry Shop", "Acrobatic Diving Pool", "Fiat dealer",
    "Patent Attorney"]

def preprocess_text(text):
    """Preprocess text by tokenizing and lemmatizing"""
    lemmatizer = WordNetLemmatizer()
    tokens = nltk.word_tokenize(text.lower())
    lemmatized_tokens = [lemmatizer.lemmatize(token, get_wordnet_pos(token)) for token in tokens]
    return lemmatized_tokens

def generate_similarity_matrix(category_list):
    """Generate similarity matrix for categories"""
    category_tokens = [preprocess_text(category) for category in category_list]
    category_vectors = get_category_vectors(get_category_tokens())
    similarity_matrix = calculate_similarity_matrix(category_vectors)
    return similarity_matrix

# Set the desired number of generalized categories
num_clusters = 35

# Generate similarity matrix
similarity_matrix = generate_similarity_matrix(category_list)

# Cluster categories
cluster_assignments = cluster_categories(similarity_matrix)

# Generalize categories
category_clusters = generalize_categories(cluster_assignments)

# Print generalized categories
print_generalized_categories(category_clusters)


