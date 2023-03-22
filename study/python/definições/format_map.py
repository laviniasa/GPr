# format_map

# O método format_map() é semelhante a str.format(**mapping), exceto que str.format(**mapping)
#  cria um novo dicionário, enquanto str.format_map(mapping) não.

point = {'x':4,'y':-5}
print('{x} {y}'.format_map(point))

point = {'x':4,'y':-5, 'z': 0}
print('{x} {y} {z}'.format_map(point))