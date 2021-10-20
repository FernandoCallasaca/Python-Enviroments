# to start to use reduce we need to import funtools library

from functools import reduce

def run():
   
   # create a list of
   L = [1,2,3,4,5]

   odd = list(filter(lambda x: x % 2 != 0, L))

   print('Odd numbers: ', odd)

   squares = list(map(lambda x: x**2, L))

   print('Squares numbers: ', squares)

   my_list = [2,2,2,2,2]
   all_multiplied = reduce(lambda a, b: a * b, my_list)
   print('Reduce: ', all_multiplied)

if __name__ == '__main__':
   run()