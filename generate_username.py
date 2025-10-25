from itertools import product

def variants(word):
    return [word, word.capitalize(), word.upper()]

# Ask user for input
name = input("Enter a name: ")
names = [name]  # Use the entered name instead of hardcoded 'sally'
roles = ['administrator', 'admin']
separators = ['', '_']

with open('usernames.txt', 'w') as f:
    for n, r, sep in product(names, roles, separators):
        for nv, rv in product(variants(n), variants(r)):
            f.write(f"{nv}{sep}{rv}\n")