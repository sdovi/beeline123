class Beeline:
    def __init__(self):
        self.tarif =   { 1: "Тариф янги, 10 минут, 10 мб, 10 смс",
                       2: "Тариф янги 2, 30 минут, 100 мб, 70 смс",
                       3: "Тариф янги 3, 50 минут, 500 мб, 150 смс"}
        self.zvon = 0
        self.mb = 0
        self.cmc = 0
class tarifi1(Beeline):
    def balance(self):
        print(f"{self.zvon} минут на звонок")
        print(f"{self.mb} мб")
        print(f"{self.cmc} смс")

    def tarif123(self):
        print(self.tarif)
        x = int(input(">>>"))
        if x == 1:
            self.zvon += 10
            self.mb += 10
            self.cmc += 10
            print("успешно оплачен")
        elif x == 2:
            self.zvon += 30
            self.mb += 100
            self.cmc += 70
            print("успешно оплачен")
        elif x == 3:
            self.zvon += 50
            self.mb += 500
            self.cmc += 150
            print("успешно оплачен")







Bank = tarifi1()
while True:
    x = (int(input("1 - просмотр баланса, 2 - тарифы, 3 - выйти.")))
    if x == 1:
        Bank.balance()
    if x == 2:
        Bank.tarif123()
    elif x == 3:
        break


