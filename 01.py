# with open("Menu.txt") as file:
#     for line in file:
#         if line.startswith("* Lütfen Bir Pizza Tabani Seçiniz:"):
#             print("Pizza Tabanlari:")
#             for line in file:
#                 if line.startswith("*"):
#                     break
#                 number, name = line.strip().split(": ")
#                 print(f"{number}: {name}")
#             base = input("Lütfen bir pizza tabani numarasi girin: ")
#         elif line.startswith("* ve seçeceğiniz sos:"):
#             print("\nSoslar:")
#             for line in file:
#                 if line.startswith("*"):
#                     break
#                 number, name = line.strip().split(": ")
#                 print(f"{number}: {name}")
#             sauce = input("Lütfen bir sos numarasi girin: ")

# print(f"Seçilen pizza tabani: {base}")
# print(f"Seçilen sos: {sauce}")

class Pizza:
    def __init__(self, description, price):
        self.description = description
        self.price = price
        
    def get_description(self):
        return self.description
        
    def get_cost(self):
        pass

class ClassicPizza(Pizza):
    def __init__(self):
        description = "Classic Pizza: tomato sauce, mozzarella cheese"
        price = 10.99
        super().__init__(description, price)
        
    def get_cost(self):
        return self.price

class MargheritaPizza(Pizza):
    def __init__(self):
        description = "Margherita Pizza: tomato sauce, mozzarella cheese, fresh basil"
        price = 12.99
        super().__init__(description, price)
        
    def get_cost(self):
        return self.price

class TurkishPizza(Pizza):
    def __init__(self):
        description = "Turkish Pizza: minced meat, onion, tomato, pepper, parsley"
        price = 15.99
        super().__init__(description, price)
        
    def get_cost(self):
        return self.price

class DominosPizza(Pizza):
    def __init__(self):
        description = "Dominos Pizza: tomato sauce, cheese, pepperoni, sausage, mushrooms"
        price = 18.99
        super().__init__(description, price)
        
    def get_cost(self):
        return self.price


#çıktı test
'''classic_pizza = ClassicPizza()
print(classic_pizza.get_description())
print(classic_pizza.get_cost())

margherita_pizza = MargheritaPizza()
print(margherita_pizza.get_description())
print(margherita_pizza.get_cost())

turkish_pizza = TurkishPizza()
print(turkish_pizza.get_description())
print(turkish_pizza.get_cost())

dominos_pizza = DominosPizza()
print(dominos_pizza.get_description())
print(dominos_pizza.get_cost())'''

class Decorator: #Decorator sınıfı
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()

class Zeytin(Decorator): # sosların sınıfları
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "zeytin"
        self._cost = 1.99

    def get_description(self):
        return self.pizza.get_description() + f", {self._description}"

    def get_cost(self):
        return self.pizza.get_cost() + self._cost


class Mantar(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "mantar"
        self._cost = 1.49

    def get_description(self):
        return self.pizza.get_description() + f", {self._description}"

    def get_cost(self):
        return self.pizza.get_cost() + self._cost


class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "keçi peyniri"
        self._cost = 2.49

    def get_description(self):
        return self.pizza.get_description() + f", {self._description}"

    def get_cost(self):
        return self.pizza.get_cost() + self._cost


class Et(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "et"
        self._cost = 3.99

    def get_description(self):
        return self.pizza.get_description() + f", {self._description}"

    def get_cost(self):
        return self.pizza.get_cost() + self._cost


class Sogan(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "soğan"
        self._cost = 0.99

    def get_description(self):
        return self.pizza.get_description() + f", {self._description}"

    def get_cost(self):
        return self.pizza.get_cost() + self._cost


class Misir(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "mısır"
        self._cost = 1.29

    def get_description(self):
        return self.pizza.get_description() + f", {self._description}"

    def get_cost(self):
        return self.pizza.get_cost() + self._cost



#main

# Menü oluşturma
menu = {
    "Klasik": ClassicPizza,
    "Margherita": MargheritaPizza,
    "Türk Pizzasi": TurkishPizza,
    "Dominos Pizza": DominosPizza
}

soslar = {
    "Zeytin": Zeytin,
    "Mantar": Mantar,
    "Keçi Peyniri": KeciPeyniri,
    "Et": Et,
    "Soğan": Sogan,
    "Misir": Misir
}
from datetime import datetime
def main():
    # Menüyü ekrana yazdırma
    print("Menü:")
    for pizza in menu:
        print("- ", pizza)
    print()
    for sos in soslar:
        print("- ", sos)
    print()

    # Kullanıcının pizza ve sos seçmesi
    pizza_secimi = input("Lütfen bir pizza seçiniz: ")
    sos_secimi = input("Lütfen bir sos seçiniz: ")

    # Seçilen pizza ve sosun nesnelerini oluşturma
    pizza_nesnesi = menu[pizza_secimi]()
    sos_nesnesi = soslar[sos_secimi](pizza_nesnesi)

    # Sipariş toplam fiyatını hesaplama
    toplam_fiyat = pizza_nesnesi.get_cost() + sos_nesnesi.get_cost()

    # Kullanıcı bilgilerini alma
    isim = input("İsim: ")
    tc_kimlik = input("TC Kimlik Numarasi: ")
    kredi_karti = input("Kredi Karti Numarasi: ")
    kredi_karti_sifre = input("Kredi Karti Şifresi: ")

    # Sipariş bilgilerini Orders_Database.csv dosyasına yazdırma
    with open("Orders_Database.csv", "a") as dosya:
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        dosya.write(f"{pizza_secimi}, {isim}, {tc_kimlik}, {kredi_karti}, {sos_secimi}, {kredi_karti_sifre}, {current_time}\n")
    
    print("Siparisiniz başariyla alindi.")

if __name__ == "__main__":
    main()

