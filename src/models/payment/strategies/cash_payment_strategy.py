from models.payment.payment_strategy import PaymentStrategy


class CashPaymentStrategy(PaymentStrategy):

    def pay(self, amount: float) -> None:
        print(f"Payment done using cash: {amount}")
