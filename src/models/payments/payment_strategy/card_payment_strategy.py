from payments.payment_strategy import PaymentStrategy


class CardPaymentStrategy(PaymentStrategy) : 


    def pay(self,amount:float):
        print(f"Payment is done using card {amount}")