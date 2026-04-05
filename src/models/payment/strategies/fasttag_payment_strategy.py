from models.payment.payment_strategy import PaymentStrategy


class FastTagPaymentStrategy(PaymentStrategy):

    def pay(self, amount: float) -> None:
        print(f"Payment done using FastTag: {amount}")
