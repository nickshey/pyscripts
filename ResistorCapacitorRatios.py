# Nojan Sheybani and James Garcia-Otero
# nds4jp and jg4ye

resistors = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2,
10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82,
100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 820,
1000, 1200, 1500, 1800, 2200, 2700, 3300, 3900, 4700, 5600, 6800, 8200,
10000, 12000, 15000, 18000, 22000, 27000, 33000, 39000, 47000, 56000, 68000, 82000,
100000, 120000, 150000, 180000, 220000, 270000, 330000, 390000, 470000, 560000, 680000, 820000, 1000000]

capacitors = [.0000001, .000000001, .0000000047, .00000001, .000000047, .000000002, .00000002, .00000000047, .0001,
              .00001, .000001, .0000047, .000022, .000047, .00022, .001, .00033]

working_resistors = []

working_capacitors = []

for i in resistors:
    for j in capacitors:
        if 1/(i*j) == 10000.0:
            working_resistors.append(i)
            working_capacitors.append(j)

print("Positions of resistors and capacitors in list is important")
print("E.g. The resistor in position 0 of the working resistors list only works with the capacitor in position 0 of "
      "the working capacitors list")
print("Resistors that work: ")
print(working_resistors)
print("Capacitors that work: ")
print(working_capacitors)