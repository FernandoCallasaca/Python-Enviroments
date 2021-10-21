# method to return divisors of one numbers
def divisors(num):
   divisors = [i for i in range(1, num + 1) if num % i == 0]
   return divisors

def run():
   # try execute my program
   try:
      num = int(input('Enter a number to know the divisors: '))
      # we ask if the number is negative
      if(num < 0):
         # if the number is negative we use 'raise' to enter a message to the ValueError Exception
         raise ValueError('Enter a positive number')
      else:
         div = divisors(num)
         print('Divisors of', num)
         for i in div:
            print(i)
   # if my program has errors
   except ValueError as ve:
      print(ve)
   # always execute this code line
   finally:
      print('Program Finished!')

if __name__ == '__main__':
   run()