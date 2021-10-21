def read():
   # to read letters like(anie , tildes)
   with open('./files/numbers.txt', 'r', encoding='utf-8') as file:
      # using list comprehension
      my_list = [int(element[:len(element)]) for element in file.readlines()]
      print('List with list comprehension:', my_list)
      # know we are in the last line
      print('Position of my cursor in the file:', file.tell())
      # to start in the first line
      file.seek(0,0)
      print('New position:',file.tell())
      # iterable for
      L = []
      for line in file:
         L.append(int(line))
      print(L)

def write():
   # create a list of names
   names = ['Fernando', 'Facundo', 'Carlos', 'Juan', 'Rocío', 'Acuña']
   # write in the file
   with open('./files/names.txt', 'w+', encoding='utf-8') as file:
      for name in names:
         file.write(name + '\n')
      file.seek(0,0)
      print(file.read())

def run():
   read()
   print()
   write()

if __name__ == '__main__':
   run()