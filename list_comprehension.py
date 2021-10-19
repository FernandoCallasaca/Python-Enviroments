def run():

   # squared numbers from 1 to 100
   L = [i**2 for i in range(1,101)]
   # print(L)

   # numbers isn't multiple of 3
   L1 = [i**2 for i in range(1,101) if i % 3 != 0]

   # print(L1)

   # numbers divisible for 4, 6 and 9
   L2 = [i for i in range(1, 10000) if ((i % 4 == 0) & (i % 6 == 0) & (i % 9 == 0))]
   print(L2)

# entry point
if __name__ == '__main__':
   run()