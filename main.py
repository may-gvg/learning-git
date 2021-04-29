print ("Hiszpańska inkwizycja' to najlepszy skecz grupy Monthy Pythona")
print ("")

lista_zakupów = {
    "Warzywniak": ['Marchew', 'Seler', 'Rukola'],
    "Piekarnia": ['Chleb', 'Pączek', 'Bułki']
}

print ("Lista Zakupów")
suma = 0
for sklep, produkty in lista_zakupów.items():
    print(f"Idę do {sklep.upper()}")
    print("kupuję tu następujące rzeczy")
    for produkt in produkty:
        print(produkt.upper())
        suma = suma + 1

print("Suma produktów: ", suma)
