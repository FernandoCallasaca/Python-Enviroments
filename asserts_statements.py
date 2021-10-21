# method to return divisors of one numbers
def divisors(num):
   divisors = [i for i in range(1, num + 1) if num % i == 0]
   return divisors

def run():
   num = input('Enter a number to know the divisors: ')
   assert num.isnumeric() and int(num) > 0, 'You need to enter a positive numbers'
   div = divisors(int(num))
   print('Divisors of', num)
   for i in div:
      print(i)
   print('Program Finished!')

if __name__ == '__main__':
   run()