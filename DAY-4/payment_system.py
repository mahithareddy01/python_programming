#polymorphism
class Payment:
    def pay(self,amount):
        print(f"Paid Rs.{amount}")
class CardPayment(Payment):
    def pay(self,amount):
        print(f"Paid Rs.{amount} using credit/debit card")
class CashPayment(Payment):
    def pay(self,amount):
        print(f"Paid Rs.{amount} in cash")
class UPIPayment(Payment):
    def pay(self,amount):
        print(f"Paid Rs.{amount} using UPI")
payments = [CashPayment(), CardPayment(), UPIPayment()]
p=Payment()
p.pay(1000)
for p in payments:
    p.pay(1000)

