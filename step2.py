# coding=utf-8
filename = "my_file.txt"
counter = 0
try:
  # Using 'x' (exclusive creation) mode will create the file if it doesn't exist.
  # If it exists, it will raise a FileExistsError.
  with open(filename, 'w+') as file:
    while counter < 100:
      counter = counter + 1
      text = str(counter)+"\n"
      file.write(text)
#    pass
except FileExistsError:
  print(" already exists")
  print('*' * 20)
