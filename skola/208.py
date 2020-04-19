from matplotlib import pyplot as plt

#----------------------START Afferent branch----------------------

#Importerar ifrån listan
text_file = open("alternativ.txt", "r")
raw_vikter = text_file.readlines()
text_file.close()

#Definerar viktklasserna
klass1 = []
klass2 = []
klass3 = []
klass4 = []
klass5 = []

#Alla vikter i float format
float_vikter = []

#----------------------END Afferent branch----------------------
#----------------------START Transform branch----------------------

#Konvertering till float
for line in raw_vikter:
    float_vikter.append(float(line))

line = None

# Viktklassifciering
for line in float_vikter:
    if line <= 5:
        klass1.append(line)
    elif line <= 10:
        klass2.append(line)
    elif line <= 15:
        klass3.append(line)
    elif line <= 20:
        klass4.append(line)
    else:
        klass5.append(line)

line = None

#Sortering av vikter i klasser
klass1.sort()
klass2.sort()
klass3.sort()
klass4.sort()
klass5.sort()

#Sortering bland alla vikter
sorterade_vikter = sorted(float_vikter)

#Uträkning av de relativa frekvenserna
rel_frekvens1 = (len(klass1)/len(float_vikter))*100
rel_frekvens2 = (len(klass2)/len(float_vikter))*100
rel_frekvens3 = (len(klass3)/len(float_vikter))*100
rel_frekvens4 = (len(klass4)/len(float_vikter))*100
rel_frekvens5 = (len(klass5)/len(float_vikter))*100

#Uträkning av de kumulerade relativa frekvenserna
kum_rel_frekvens1 = rel_frekvens1
kum_rel_frekvens2 = rel_frekvens1 + rel_frekvens2
kum_rel_frekvens3 = rel_frekvens1 + rel_frekvens2 + rel_frekvens3
kum_rel_frekvens4 = rel_frekvens1 + rel_frekvens2 + rel_frekvens3 + rel_frekvens4
kum_rel_frekvens5 = rel_frekvens1 + rel_frekvens2 + rel_frekvens3 + rel_frekvens4 + rel_frekvens5

#Utrkäning av Median

half = len(sorterade_vikter)/2
half = int(half)
median = sorterade_vikter[half]

#----------------------END Transform branch----------------------
#----------------------START Efferent branch----------------------

#Alla Klasser (ordnade)
print("\n\nBagage som är lättare än 5 Kg: \n")
for line in klass1:
    print(line, "Kg")

print("\n\nBagage som är mellan 5 och 10 Kg: \n")
for line in klass2:
    print(line, "Kg")

print("\n\nBagage som är mellan 10 och 15 Kg: \n")
for line in klass3:
    print(line, "Kg")

print("\n\nBagage som är mellan 15 och 20 Kg: \n")
for line in klass4:
    print(line, "Kg")

print("\n\nBagage som är över 20 Kg: \n")
for line in klass5:
    print(line, "Kg")

line = None

# Frekvenser
print("\n\n\nFrekvenser för dom olika klasserna:\n")

print("Klass 1 (0 - 5 Kg):", len(klass1))
print("Klass 2 (5 - 10 Kg):", len(klass2))
print("Klass 3 (10 - 15 Kg):", len(klass3))
print("Klass 4 (15 - 20 Kg):", len(klass4))
print("Klass 5 (över 20 Kg):", len(klass5))
print("\nDet finns", len(float_vikter), "bagage totalt.")

#Relativa frekvenser
print("\n\n\nRelativa Frekvenser för dom olika klasserna:\n")

print("Klass 1 (under 5 Kg)", round(rel_frekvens1, 1) , "%.")
print("Klass 2 (5 - 10 Kg)", round(rel_frekvens2, 1) , "%.")
print("Klass 3 (10 - 15 Kg)", round(rel_frekvens3, 1) , "%.")
print("Klass 4 (15 - 20 Kg)", round(rel_frekvens4, 1) , "%.")
print("Klass 5 (över 20 Kg)", round(rel_frekvens5, 1) , "%.")

#Kumulerade frekvenser
print("\n\n\nDe Kumulerade frekvenserna:\n")

print("Klass 1 (0 - 5 Kg):", len(klass1))
print("Klass 2 (5 - 10 Kg):", len(klass2) + len(klass1))
print("Klass 3 (10 - 15 Kg):", len(klass3) + len(klass2) + len(klass1))
print("Klass 4 (15 - 20 Kg):", len(klass4) + len(klass3) + len(klass2) + len(klass1))
print("Klass 5 (över 20 Kg):", len(klass5) + len(klass4) + len(klass3) + len(klass2) + len(klass1))

#Relativa kumulerade frekvenser
print("\n\n\nRelativa kumulerade frekvenser för dom olika klasserna:\n")

print("Klass 1 (under 5 Kg)", round(kum_rel_frekvens1, 1), "%.")
print("Klass 2 (5 - 10 Kg)", round(kum_rel_frekvens2, 1), "%.")
print("Klass 3 (10 - 15 Kg)", round(kum_rel_frekvens3, 1), "%.")
print("Klass 4 (15 - 20 Kg)", round(kum_rel_frekvens4, 1), "%.")
print("Klass 5 (över 20 Kg)", round(kum_rel_frekvens5, 1), "%.")

#Median
print("\n\n\nMedian:\n")

print(median)


x = [1, 2, 3, 4, 5]
y = [len(klass1), len(klass2), len(klass3), len(klass4), len(klass5)]

plt.bar(x, y, label="Frekvenser")

plt.xlabel("Viktklasser")
plt.ylabel("Frekvenser")
plt.title("Frekvens av olika viktklasser")
plt.legend()
plt.show()


#----------------------END Efferent branch----------------------
