from functools import lru_cache

@lru_cache(100)
def num(name):
  return int(input(f'Number of {name}: '))

coded_colors = {
  'r': 'red',
  'g': 'green',
  'b': 'blue',
  'y': 'yellow',
  'w': 'white',
  'd': 'black',
}
