# -*- coding: utf-8 -*-
"""UTS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DnrvZ9HWw9dt3xVdJ4-hSFTQH8KN7-9D
"""

nama = "Fathimatuzzahro"
nim = "V3420032"
asal = "Purworejo"
hobi = "Menonton anime"
cita = "Software Developer"
print ("Biodata", "\nNama Mahasiswa : ", nama, "\nNIM : ", nim, "\nAsal : ", asal, "\nHobi : ", hobi, "\nCita - cita : ", cita)

s = 15
LP = 6 * s * s
print(" Luas Permukaan Kubus adalah : "+ str(LP))

string = ""
bar = 1
x = int(input("Masukkan angka :"))

# Looping Baris
while bar <= x:
  kol = bar

	# Looping Kolom
  while kol > 0:
    string = string + " * "
    kol = kol - 1

  string = string + "\n"
  bar = bar + 1
  
print (string)

bilangan = [27, 54, 47, 30, 94, 67, 33]
genap=0
ganjil=0
bil_genap = []
bil_ganjil = []
for bilangan in bilangan :
  if bilangan % 2 == 0 :
    bil_genap.append(bilangan)
    genap+=1
  else :
    bil_ganjil.append(bilangan)
    ganjil+=1
print('genap: {}'.format(','.join([str(bilangan)for bilangan in bil_genap])))
print("Jumlah bilangan genap : ", genap)
print("")
print('ganjil: {}'.format(','.join([str(bilangan)for bilangan in bil_ganjil])))
print("Jumlah bilangan ganjil : ", ganjil)

d = {'a': 27, 'b': 54, 'c': 47, 'd': 30, 'e': 94, 'f': 67, 'g': 33}
jml = sum(list(d.values()))
print(jml)