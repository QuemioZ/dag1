print('start met csv uitlees applicatie')

import pandas

df = pandas.read_csv('pokemon.csv')
print(df["name"])