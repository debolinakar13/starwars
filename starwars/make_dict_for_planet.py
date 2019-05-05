import pickle
import requests
urls = ['https://swapi.co/api/planets', 'https://swapi.co/api/films']

for req in urls:
    _file = req.rsplit('/')[-1] + '.pickle'
    req = requests.get(req)
    data = req.json()['results']

    while req.json()['next']:
        req = requests.get(req.json()['next'])
        data.extend(req.json()['results'])
    a = {}
    for rec in data:
        try:
            a[rec['name'].lower()] = rec
        except:
            a[rec['title'].lower()] = rec
    with open(_file, 'wb') as handle:
        pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)
