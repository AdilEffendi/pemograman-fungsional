def triangular(a):
  temp = 0
  for i in range(a):
    temp += a
    a -= 1

    return temp

print("Hasil dari triangular 5 = " + str(triangular(5)))