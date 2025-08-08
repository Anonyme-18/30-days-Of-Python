names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

# Unpack the first five countries into nordic_countries, and the last two into es and ru
*nordic_countries, es, ru = names

print("Nordic countries:", nordic_countries)
print("Estonia:", es)
print("Russia:", ru)
