class Beeline:
    def __init__(self):
        self.balance = 20000
        self.tarif = {
            1: "Тариф янги, 10 минут, 10 мб, 10 смс(5000 сум, Код *150# )",
            2: "Тариф янги 2, 30 минут, 100 мб, 70 смс(10000 сум, Код *200#)",
            3: "Тариф янги 3, 50 минут, 500 мб, 150 смс(25000 сум, Код *95#)"}
        self.zvon = 0
        self.mb = 0
        self.cmc = 0


class Tarifi1(Beeline):
    def balance_show(self):
        print(f"{self.balance} денег")
        print(f"{self.zvon} минут на звонок")
        print(f"{self.mb} мб")
        print(f"{self.cmc} смс")

    def prosmotr(self):
        print("у нас есть")
        print(f"{self.tarif[1]}"
              f"{self.tarif[2]}"
              f"{self.tarif[3]}")

    def tarif123(self):
        print(self.tarif)
        user_choice = input(">>>")
        if user_choice == "*150#" and self.balance >= 5000:
            self.balance -= 5000
            self.zvon += 10
            self.mb += 10
            self.cmc += 10
            print("успешно оплачен")
        elif self.balance != 5000:
            print("не хватает денег")
        elif user_choice == "*200#" and self.balance >= 10000:
            self.balance -= 1000
            self.zvon += 30
            self.mb += 100
            self.cmc += 70
            print("успешно оплачен")
        elif self.balance != 10000:
            print("не хватает денег")

            if user_choice == "*95#" and self.balance == 25000:
                self.zvon += 50
                self.mb += 500
                self.cmc += 150
                print("успешно оплачен")
            elif self.balance != 25000:
                print("не хватает денег")


Bank = Tarifi1()
while True:
    x = (int(input("1 - просмотр баланса, 2 - просмотр, 3 - поменять тариф 4 - выход.")))
    if x == 1:
        Bank.balance_show()
    elif x == 2:
        Bank.prosmotr()
    elif x == 3:
        Bank.tarif123()
    elif x == 4:
        break
    else:
        print("выберайте между 1-4")

