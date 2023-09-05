from imperative import selection_sort
from declarative import builtin_sort

default = [6, 25, 12, 22, 11]

print("Default list:\t", default)
print("Imperative:\t", selection_sort(default))
print("Declarative:\t", builtin_sort(default))