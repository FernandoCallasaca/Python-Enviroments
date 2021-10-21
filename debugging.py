# method to return divisors of one numbers
def divisors(num):
   divisors = [i for i in range(1, num + 1) if num % i == 0]
   return divisors

def run():
   # in this case we use visual studio code
   # so vscode has an option called Run and Debug
   # we use this option to start debugging my Program
   num = int(input('Enter a number to know the divisors: '))
   div = divisors(num)
   print('Divisors of', num)
   for i in div:
      print(i)

   print('Program Finished!')

if __name__ == '__main__':
   run()