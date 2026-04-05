from payments.payment_strategy import PaymentStrategy


class FastTagPaymentStrategy(PaymentStrategy): 

    def pay(self,amount:float):
        print(f"Payment is done using FastTag {amount}")

    