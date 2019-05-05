import pickle

planets = {}
films = {}

with open('planets.pickle', 'rb') as handle:
    planets = pickle.load(handle)

with open('films.pickle', 'rb') as handle:
    films = pickle.load(handle)

