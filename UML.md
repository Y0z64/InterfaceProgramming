## UML Diagram
```mermaid
classDiagram
    class PaymentDetails {
        +float amount
        +str currency
        +str description
        +str transaction_id
        +datetime timestamp
        +str status
    }

    class Payment {
        <<interface>>
        +process_payment(amount: float, currency: str) PaymentDetails
        +refund(transaction_id: str) bool
        +get_status(transaction_id: str) str
        +validate_payment(amount: float) bool
    }

    class PaymentProcessor {
        -Payment payment_provider
        +__init__(payment_provider: Payment)
        +process_transaction(amount: float, currency: str) PaymentDetails
        +request_refund(transaction_id: str) bool
        +check_status(transaction_id: str) str
    }

    class PayPalPayment {
        -str client_id
        -str client_secret
        -Dict transactions
        +__init__(client_id: str, client_secret: str)
        +process_payment(amount: float, currency: str) PaymentDetails
        +refund(transaction_id: str) bool
        +get_status(transaction_id: str) str
        +validate_payment(amount: float) bool
    }

    class CreditCardPayment {
        -str merchant_id
        -str api_key
        -Dict transactions
        +__init__(merchant_id: str, api_key: str)
        +process_payment(amount: float, currency: str) PaymentDetails
        +refund(transaction_id: str) bool
        +get_status(transaction_id: str) str
        +validate_payment(amount: float) bool
    }

    class BankTransferPayment {
        -str bank_id
        -str account_number
        -Dict transactions
        +__init__(bank_id: str, account_number: str)
        +process_payment(amount: float, currency: str) PaymentDetails
        +refund(transaction_id: str) bool
        +get_status(transaction_id: str) str
        +validate_payment(amount: float) bool
    }

    Payment <|.. PayPalPayment
    Payment <|.. CreditCardPayment
    Payment <|.. BankTransferPayment
    PaymentProcessor o-- Payment
    PayPalPayment ..> PaymentDetails
    CreditCardPayment ..> PaymentDetails
    BankTransferPayment ..> PaymentDetails
```

## PNG
![alt text](mermaid-diagram-2025-02-22-230639.png)