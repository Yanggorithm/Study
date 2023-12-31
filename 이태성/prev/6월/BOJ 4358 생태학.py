import sys
input = sys.stdin.readline
species = dict()
while True:
    one_species = input().strip()
    if len(one_species) == 0:
        break
    if species.get(one_species):
        species[one_species] += 1
    else:
        species[one_species] = 1

cnt_species = sum(species.values())
for now in sorted(species.keys()):
    print("%s %.4f" %(now, (species[now]/cnt_species)*100))