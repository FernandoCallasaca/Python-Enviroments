def run():
   # One list
   my_list = [1, 'Hello', True, 4.5]
   # One dictionary
   my_dict = {'firstname': 'Fernando', 'lastname': 'Callasaca'}

   # Lists of dictionaries
   super_list =[
      {'firstname': 'Fernando', 'lastname': 'Callasaca'},
      {'firstname': 'Miguel', 'lastname': 'Torres'},
      {'firstname': 'Pepe', 'lastname': 'Rodelo'},
      {'firstname': 'Susana', 'lastname': 'Martinez'},
      {'firstname': 'José', 'lastname': 'García'}
   ]

   # Dictionary of lists
   super_dict = {
      'natural_nums': [1,2,3,4,5],
      'integer_nums': [-1,-2,0,1,2],
      'floating_nums': [1.1,4.5,6.43]
   }

   for key, value in super_dict.items():
      print(key, '-', value)

   print()

   for i in super_list:
      print(i)

# Star the function
if __name__ == '__main__':
   run()