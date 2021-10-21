# import reduce to functools library
from functools import reduce

# our data list of dictionaries
# in this case I create a variable with uppercase
# so in this case for me is constant
DATA = [
   {
      'name': 'Facundo',
      'age': 72,
      'organization': 'Platzi',
      'position': 'Technical Coach',
      'language': 'python',
   },
   {
      'name': 'Luisana',
      'age': 33,
      'organization': 'Globant',
      'position': 'UX Designer',
      'language': 'javascript',
   },
   {
      'name': 'Héctor',
      'age': 19,
      'organization': 'Platzi',
      'position': 'Associate',
      'language': 'ruby',
   },
   {
      'name': 'Gabriel',
      'age': 20,
      'organization': 'Platzi',
      'position': 'Associate',
      'language': 'javascript',
   },
   {
      'name': 'Isabella',
      'age': 30,
      'organization': 'Platzi',
      'position': 'QA Manager',
      'language': 'java',
   },
   {
      'name': 'Karo',
      'age': 23,
      'organization': 'Everis',
      'position': 'Backend Developer',
      'language': 'python',
   },
   {
      'name': 'Ariel',
      'age': 32,
      'organization': 'Rappi',
      'position': 'Support',
      'language': '',
   },
   {
      'name': 'Juan',
      'age': 17,
      'organization': '',
      'position': 'Student',
      'language': 'go',
   },
   {
      'name': 'Pablo',
      'age': 32,
      'organization': 'Master',
      'position': 'Human Resources Manager',
      'language': 'python',
   },
   {
      'name': 'Lorena',
      'age': 56,
      'organization': 'Python Organization',
      'position': 'Language Maker',
      'language': 'python',
   },
]

# create our function run
def run():
   # create a list to python devs - list comprehension
   all_python_devs = [i['name'] for i in DATA if i['language'].upper() == 'PYTHON']
   print('Python Devs:', all_python_devs)

   # workers from Platzi - list comprehension
   all_workers_platzi = [worker['name'] for worker in DATA if worker['organization'].lower() == 'platzi']
   print('Workers Platzi: ', all_workers_platzi)

   # list adult person +18 - filter and map (high order function)
   # all_adult_people = [person['name'] for person in DATA if person['age'] > 18]
   all_adult_people = list(filter(lambda worker: worker['age'] > 18, DATA))
   all_adult_people = list(map(lambda worker: worker['name'], all_adult_people))
   print('Adult People:', all_adult_people)

   # create a new list of dictionaries with one new attribute add(True, False) if is old +70
   # using high order functions
   new_list = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))
   print('New list:', new_list)

   print('\nRETO\n')

   #################### RETO
   # create a list to python devs - high order function
   python_devs = list(filter(lambda worker: worker['language'].upper() == 'PYTHON', DATA))
   python_devs = list(map(lambda worker: worker['name'], python_devs))
   print('Python Devs:', python_devs)

   # workers from Platzi - high order function
   platzi_workers = list(filter(lambda worker: worker['organization'].lower() == 'platzi', DATA))
   platzi_workers = list(map(lambda worker: worker['name'], platzi_workers))
   print('Platzi Workers:', platzi_workers)

   # list adult person +18 - list comprehension
   # all_adult_people = [person['name'] for person in DATA if person['age'] > 18]
   adult_workers = [worker['name'] for worker in DATA if worker['age'] > 18]
   print('Adult Workers:', adult_workers)

   # create a new list of dictionaries with one new attribute add(True, False) if is old +70
   # using list comprehension
   my_new_list = [my_dict | {'old': my_dict['age'] > 70} for my_dict in DATA]
   print('My new list:', my_new_list)

# create our entrypoints
if __name__ == '__main__':
   run()