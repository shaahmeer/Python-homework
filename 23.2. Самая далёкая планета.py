def find_farthest_orbit(orb):
    sp = []
    for i in orb:
        sp.append(i[0] * i[1])
    ind = sp.index(max(sp))
    a, b = orb[ind]
    print(a, b)

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))