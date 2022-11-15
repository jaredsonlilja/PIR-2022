
# Filtre vmax et vmin
liste = [34.6, 25.4, 32.3, 45.4, 42.2, 20.2]
conso = [0.0, 0.07, 0.1, 0.0]
def condition(x):
    return x > 23.0 and x < 35.0

résultat= [x for x in liste if condition(x)]
print(résultat)
