from abc import ABC, abstractmethod
from typing import Dict, Optional
from datetime import datetime
from dataclasses import dataclass
from enum import Enum

class PaymentStatus(Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    REFUNDED = "REFUNDED"

@dataclass
class PaymentDetails:
    amount: float
    currency: str
    description: str
    transaction_id: str
    timestamp: datetime
    status: PaymentStatus = PaymentStatus.PENDING

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount: float, currency: str = "USD") -> PaymentDetails:
        """
        Process a payment with the specified amount and currency.
        Args:
            amount: The amount to process
            currency: The currency code (default: USD)
        Returns:
            PaymentDetails: Details of the processed payment
        """
        pass

    @abstractmethod
    def refund(self, transaction_id: str) -> bool:
        """
        Refund a specific transaction.
        Args:
            transaction_id: The ID of the transaction to refund
        Returns:
            bool: True if refund was successful, False otherwise
        """
        pass

    @abstractmethod
    def get_status(self, transaction_id: str) -> PaymentStatus:
        """
        Get the status of a transaction.
        Args:
            transaction_id: The transaction ID to check
        Returns:
            PaymentStatus: The current status of the transaction
        """
        pass

    @abstractmethod
    def validate_payment(self, amount: float) -> bool:
        """
        Validate if a payment amount is valid for this payment method.
        Args:
            amount: The amount to validate
        Returns:
            bool: True if the amount is valid, False otherwise
        """
        pass

class PaymentProcessor:
    def __init__(self, payment_provider: Payment):
        self.payment_provider = payment_provider

    def process_transaction(self, amount: float, currency: str = "USD") -> PaymentDetails:
        if not self.payment_provider.validate_payment(amount):
            raise ValueError(f"Invalid payment amount: {amount}")
        
        return self.payment_provider.process_payment(amount, currency)

    def request_refund(self, transaction_id: str) -> bool:
        return self.payment_provider.refund(transaction_id)

    def check_status(self, transaction_id: str) -> PaymentStatus:
        return self.payment_provider.get_status(transaction_id)

class PayPalPayment(Payment):
    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.transactions: Dict[str, PaymentDetails] = {}

    def validate_payment(self, amount: float) -> bool:
        return amount > 0 and amount <= 10000

    def process_payment(self, amount: float, currency: str = "USD") -> PaymentDetails:
        # Aquí iría la lógica real de integración con PayPal
        transaction_id = f"PP_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        payment_details = PaymentDetails(
            amount=amount,
            currency=currency,
            description="PayPal payment",
            transaction_id=transaction_id,
            timestamp=datetime.now(),
            status=PaymentStatus.COMPLETED
        )
        self.transactions[transaction_id] = payment_details
        print(f"Processing PayPal payment of {amount} {currency}")
        return payment_details

    def refund(self, transaction_id: str) -> bool:
        if transaction_id in self.transactions:
            self.transactions[transaction_id].status = PaymentStatus.REFUNDED
            print(f"Refunding PayPal transaction {transaction_id}")
            return True
        return False

    def get_status(self, transaction_id: str) -> PaymentStatus:
        if transaction_id in self.transactions:
            return self.transactions[transaction_id].status
        return PaymentStatus.FAILED

class CreditCardPayment(Payment):
    def __init__(self, merchant_id: str, api_key: str):
        self.merchant_id = merchant_id
        self.api_key = api_key
        self.transactions: Dict[str, PaymentDetails] = {}

    def validate_payment(self, amount: float) -> bool:
        return amount > 0 and amount <= 5000

    def process_payment(self, amount: float, currency: str = "USD") -> PaymentDetails:
        transaction_id = f"CC_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        payment_details = PaymentDetails(
            amount=amount,
            currency=currency,
            description="Credit Card payment",
            transaction_id=transaction_id,
            timestamp=datetime.now(),
            status=PaymentStatus.COMPLETED
        )
        self.transactions[transaction_id] = payment_details
        print(f"Processing Credit Card payment of {amount} {currency}")
        return payment_details

    def refund(self, transaction_id: str) -> bool:
        if transaction_id in self.transactions:
            self.transactions[transaction_id].status = PaymentStatus.REFUNDED
            print(f"Refunding Credit Card transaction {transaction_id}")
            return True
        return False

    def get_status(self, transaction_id: str) -> PaymentStatus:
        if transaction_id in self.transactions:
            return self.transactions[transaction_id].status
        return PaymentStatus.FAILED

class BankTransferPayment(Payment):
    def __init__(self, bank_id: str, account_number: str):
        self.bank_id = bank_id
        self.account_number = account_number
        self.transactions: Dict[str, PaymentDetails] = {}

    def validate_payment(self, amount: float) -> bool:
        return amount > 0 and amount <= 50000

    def process_payment(self, amount: float, currency: str = "USD") -> PaymentDetails:
        transaction_id = f"BT_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        payment_details = PaymentDetails(
            amount=amount,
            currency=currency,
            description="Bank Transfer payment",
            transaction_id=transaction_id,
            timestamp=datetime.now(),
            status=PaymentStatus.PROCESSING
        )
        self.transactions[transaction_id] = payment_details
        print(f"Processing Bank Transfer payment of {amount} {currency}")
        return payment_details

    def refund(self, transaction_id: str) -> bool:
        if transaction_id in self.transactions:
            self.transactions[transaction_id].status = PaymentStatus.REFUNDED
            print(f"Refunding Bank Transfer transaction {transaction_id}")
            return True
        return False

    def get_status(self, transaction_id: str) -> PaymentStatus:
        if transaction_id in self.transactions:
            return self.transactions[transaction_id].status
        return PaymentStatus.FAILED

def main():
    # Crear instancias de los proveedores de pago
    paypal = PayPalPayment("client_id", "client_secret")
    credit_card = CreditCardPayment("merchant_id", "api_key")
    bank_transfer = BankTransferPayment("bank_123", "acc_456")

    # Crear procesadores de pago
    paypal_processor = PaymentProcessor(paypal)
    cc_processor = PaymentProcessor(credit_card)
    bank_processor = PaymentProcessor(bank_transfer)

    # Procesar pagos
    try:
        # Pago con PayPal
        pp_payment = paypal_processor.process_transaction(100.00, "USD")
        print(f"PayPal Status: {paypal_processor.check_status(pp_payment.transaction_id)}")
        
        # Pago con tarjeta de crédito
        cc_payment = cc_processor.process_transaction(50.00, "EUR")
        print(f"Credit Card Status: {cc_processor.check_status(cc_payment.transaction_id)}")
        
        # Pago con transferencia bancaria
        bt_payment = bank_processor.process_transaction(1000.00, "USD")
        print(f"Bank Transfer Status: {bank_processor.check_status(bt_payment.transaction_id)}")

        # Reembolsos
        print(f"PayPal Refund: {paypal_processor.request_refund(pp_payment.transaction_id)}")
        print(f"New PayPal Status: {paypal_processor.check_status(pp_payment.transaction_id)}")

    except ValueError as e:
        print(f"Error processing payment: {e}")

if __name__ == "__main__":
    main()