
from payments.payment_strategy import PaymentStrategy


class CashPaymentStrategy(PaymentStrategy):

    def pay(self,amount:float):
        print(f"Payment is done using cash {amount}")