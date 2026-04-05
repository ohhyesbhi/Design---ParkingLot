from models.payment.payment_strategy import PaymentStrategy


class CardPaymentStrategy(PaymentStrategy):

    def pay(self, amount: float) -> None:
        print(f"Payment done using card: {amount}")
