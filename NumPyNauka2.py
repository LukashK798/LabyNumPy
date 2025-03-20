import numpy as np
# #Zadanie 1
# arr = np.array(["python", "NumPy", "data science", "machine learning"])
# print(np.char.upper(arr))
#
# #Zadanie 2
# print(np.char.lower(arr))
# print(np.char.title(arr))

# #Zadanie 3
# arr1 = np.array(["machine", "deep"])
# arr2 = np.array(["learning", "networks"])
# combined = np.char.add(arr1, arr2)
# combined = np.char.replace(combined, "_", " ")
# print(combined)

# # Zadanie 4
# arr = np.array(["python.data.science", "machine.learning"])
# split = np.char.split(arr, ".")
# print(split)

# # Zadanie 5
# arr = np.array([" python ", " numpy ", " pandas "])
# stripped = np.char.strip(arr)
# print(stripped)

# # Zadanie 6
# a = np.array([2, 4, 6])
# b = np.array([1, 3, 5])
# scalar_product = np.dot(a, b)
# print(scalar_product)

# # Zadanie 7
# A = np.array([[2, 3], [1, 4]])
# B = np.array([[5, 1], [2, 6]])
# matrix_product = np.matmul(A, B)
# print(matrix_product)

# # Zadanie 8
# A = np.array([[4, 2], [3, 5]])
# b = np.array([8, 7])
# x = np.linalg.solve(A, b)
# print(x)

# # Zadanie 9
# M = np.array([[6, 2], [3, 9]])
# det = np.linalg.det(M)
# inv = np.linalg.inv(M)
# print("Wyznacznik:", det)
# print("Macierz odwrotna:\n", inv)
# identity_check = np.matmul(M, inv)
# print("Sprawdzenie macierzy jednostkowej:\n", identity_check)

# # Zadanie 10
# v1 = np.array([1, 2, 3])
# v2 = np.array([4, 5, 6])
# outer_product = np.outer(v1, v2)
# eigenvalues, eigenvectors = np.linalg.eig(outer_product)
# print("Iloczyn zewnętrzny:\n", outer_product)
# print("Wartości własne:\n", eigenvalues)
# print("Wektory własne:\n", eigenvectors)
#
# # Zadanie 11
# arr = np.array([[0, 5, 0], [2, 0, 3], [0, 0, 7]])
# nonzero_indices = np.nonzero(arr)
# print("Indeksy elementów niezerowych:", nonzero_indices)
# print("Wartości niezerowe:", arr[nonzero_indices])
#
# # Zadanie 12
# data = np.array([-3, 4, -1, 6, -8, 2])
# modified = np.where(data < 0, -99, data)
# print("Zmodyfikowana tablica:", modified)
#
# # Zadanie 13
# indices = np.array([2, 0, 1, 2, 0])
# options = [np.array([10, 20, 30, 40, 50]), np.array([60, 70, 80, 90, 100]), np.array([110, 120, 130, 140, 150])]
# result = np.choose(indices, options)
# print("Nowa tablica:", result)

# #Zadanie 14
# matrix = np.array([[5, 12, 8], [3, 9], [15, 4, 2]])
# conditions = [matrix < 5, (matrix >= 5) & (matrix <= 10), matrix > 10]
# choices = [0, 50, 100]
# new_matrix = np.select(conditions, choices)
# print("Zmieniona macierz:\n", new_matrix)

# Zadanie 15
values = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

np.putmask(values, values % 2 == 0, 0)
print("Po zastosowaniu np.putmask():", values)

np.put(values, [0, 4, 8], [100, 200, 300])
print("Po zastosowaniu np.put():", values)
