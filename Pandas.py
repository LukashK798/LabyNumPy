import pandas as pd

# Zadanie 1
# a)
seria = pd.Series([15, 28, 33, 47, 52, 61])
print(seria.to_numpy())
print(seria.values)

# b)
print(type(seria.to_numpy()))
print(type(seria.values))

# c)
print(seria[seria > 40])

# Zadanie 2
owoce = pd.Series({'jablka': 120, 'gruszki': 85, 'sliwki': 95, 'banany': 140})

# a)
owoce.name = "Owoce"
owoce.index.name = "Produkt"

# b)
print("Wartosc dla 'gruszki':", owoce['gruszki'])

# c)
owoce['gruszki'] = 110

# d)
owoce_zwiekszone = owoce * 2
print("Pomnożona seria przez 2:")
print(owoce_zwiekszone)

# Zadanie 3
d = {'klucz1': 50, 'klucz2': 100, 'klucz3': 150}
k = ['klucz0', 'klucz2', 'klucz3', 'klucz4']

seria = pd.Series(d, index=k)

#a)
print("Utworzona seria:")
print(seria)

#b)
print("\nWyjaśnienia:")
print(f"Klucz 'klucz0': {seria['klucz0']}")
print(f"Klucz 'klucz4': {seria['klucz4']}")

#c)
seria.name = "Wartości"
seria.index.name = "Klucz"

#Zadanie 4
# Dane
data = {'Student': ['Anna', 'Bartek', 'Celina', 'Daniel'],
        'Matematyka': [4.5, 3.5, 5.0, 3.0],
        'Fizyka': [4.0, 4.5, 3.5, 3.0],
        'Informatyka': [5.0, 3.0, 4.5, 4.0]}

# Ramka danych
df = pd.DataFrame(data)

# Kształt ramki danych
print("Kształt ramki danych:", df.shape)

# Indeks ramki
print("Indeks ramki danych:", df.index)

# Kolumny ramki
print("Kolumny ramki danych:", df.columns)

# Informacje o ramce danych
df.info()

# Liczba niepustych wartości w każdej kolumnie
print(df.count())

#Zadanie 5
# Dane
data = {'Kraj': ['Polska', 'Niemcy', 'Francja'],
        'Stolica': ['Warszawa', 'Berlin', 'Paryż'],
        'Populacja': [38000000, 83000000, 67000000]}

# Ramka danych
df = pd.DataFrame(data)

# Początkowy wiersz i początkową kolumnę
print("Początkowy wiersz:\n", df.iloc[0])
print(df['Kraj'])

# Wiersz o indeksie 2
print(df.iloc[2])

# Kolumna 'Stolica'
print(df['Stolica'])

# Wartość w wierszu o indeksie 1 i kolumnie 'Stolica'
print(df.loc[1, 'Stolica'])

#Zadanie 6
# Dane
data = {'Region': ['Północ', 'Południe', 'Wschód', 'Zachód', 'Północ', 'Południe'],
        'Produkt': ['A', 'A', 'A', 'A', 'B', 'B'],
        'Sprzedaż': [150, 200, 130, 180, 220, 170]}

# Ramka danych
df = pd.DataFrame(data)

# Kolumna 'Sprzedaż'
print(df['Sprzedaż'])

# Wiersze gdzie sprzedaż jest większa niż 180
print(df[df['Sprzedaż'] > 180])

#Zadanie 7
# Dane
data = {
    'Region': ['North', 'South', 'East', 'West', 'North', 'South'],
    'Product': ['Electronics', 'Furniture', 'Clothing', 'Electronics',
                'Furniture', 'Clothing'],
    'Sales_Channel': ['Online', 'Retail', 'Online', 'Wholesale',
                      'Retail', 'Online'],
    'Units_Sold': [120, 80, 200, 150, 90, 300],
    'Revenue': [60.5, 45.0, 35.0, 70.0, 50.5, 55.0],
    'Profit': [15.2, 12.0, 8.5, 20.5, 13.2, 10.0]
}

# Ramka danych
sales_df = pd.DataFrame(data)

# Kolumna 'Revenue'
print(sales_df['Revenue'])

# Wiersze gdzie 'Profit' jest większy niż 15.0
print(sales_df[sales_df['Profit'] > 15.0])

# Tylko kolumna 'Revenue' wierszy z poprzedniego punktu
print(sales_df[sales_df['Profit'] > 15.0]['Revenue'])

# Znajdujemy i wyświetlamy wiersz o najwyższym przychodzie ('Revenue')
max_revenue_row = sales_df[sales_df['Revenue'] == sales_df['Revenue'].max()]
print(max_revenue_row)

# Nowa kolumna 'Revenue_per_Unit'
sales_df['Revenue_per_Unit'] = sales_df['Revenue'] / sales_df['Units_Sold']
print(sales_df)
