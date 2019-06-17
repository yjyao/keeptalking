from functools import lru_cache
import re

@lru_cache(100)
def num(name):
  return int(input(f'Number of {name}: '))

@lru_cache(1)
def serial_ends_with_odd():
  return int(input(f'Last digit of serial number: ')) % 2 != 0

def yesno(prompt):
  return re.match('yes|y', input(f'{prompt} [Y/n] ').lower()) is not None

coded_colors = {
  'r': 'red',
  'g': 'green',
  'b': 'blue',
  'y': 'yellow',
  'w': 'white',
  'd': 'black',
}
