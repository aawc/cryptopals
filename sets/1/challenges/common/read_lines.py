def ReadLines(filename):
  content = []
  with open(filename) as f:
    content = [x.rstrip() for x in f.readlines()]
  return content

