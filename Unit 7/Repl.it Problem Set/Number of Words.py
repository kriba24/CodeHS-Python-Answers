def hello(name):
  counter = 1
  name = name.strip()
  for i in range(len(name)):
    if name[i] == " ":
      counter += 1
  return counter