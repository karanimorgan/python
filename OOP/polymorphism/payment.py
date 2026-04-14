class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement this method.")
    
class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f"Paid{amount} using a credit card."

class Paypal(PaymentMethod):
    def pay(self,amount):
        return f"paid {amount} using PayPal." 

class Mpesa(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} using M-Pesa."
    
class Banktransfer(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} using bank transfer."
    
Payment_methods = {
    "credit_card": CreditCard(),
    "paypal": Paypal(),
    "mpesa": Mpesa(),
    "bank_transfer": Banktransfer()
}

choice = input("chooose a payment method(credit_card, paypal, mpesa, bank_transfer): ")
if choice in Payment_methods:
    amount = float(input("Enter the amount to pay:"))
    print(Payment_methods[choice].pay(amount))
else:
    print("Invalid payment method selected.")