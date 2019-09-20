#invoer
aantal_deeltjes_in_mol = input('geef aantal deeltjes')
n_a = 6.020*10**23
m_s = 32.06

#berekening
massa = m_s * float(aantal_deeltjes_in_mol)
aantal_deeltjes = float(aantal_deeltjes_in_mol) * n_a

#uitvoer
print(massa)
print(aantal_deeltjes)

