# coding=utf-8
filename = "my_file.txt"
counter = 0
with open(filename, 'w') as file:
  while counter < 100:
    counter = counter + 1
    text = str(counter)+"\n"
    file.write(text)
