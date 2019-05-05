# Starwars API

- Create virtualenv
**Run Command**
```
virtualenv -p python2 <virtualenv-name>
```
- Run the following command to install all the requirements
**Run Command**
```
pip install -r requirements.txt
```

- To run the server use following command
**Run Command**
```
python manage.py runserver 0:8000
```

### The make_dict_for_planet.py script will contact the swapi to make pickle file for the films and planets. So that the results can be fetched from the pickle file instead of requesting the swapi everytime. That will increase up the speed for computation.
