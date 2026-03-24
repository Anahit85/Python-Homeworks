# 1. Multi-Currency Bank System
#
# Դու պետք է կառուցես բանկային համակարգ, որտեղ օգտատերերը ունեն տարբեր արժույթներով հաշիվներ (օրինակ՝ USD, EUR, AMD)
# և կարող են փոխանցումներ կատարել միմյանց միջև։
#
# Համակարգը պետք է պահի յուրաքանչյուր հաշվի մնացորդը և արժույթը, ինչպես նաև բոլոր գործողությունների
# պատմությունը (deposit, withdraw, transfer)։
#
# Պետք է ապահովել, որ՝
#
# հաշվի գումարը երբեք բացասական չդառնա
# փոխանցման ժամանակ, եթե արժույթները տարբեր են, կատարվի ավտոմատ փոխակերպում նախապես սահմանված փոխարժեքներով
# եթե փոխարժեք չկա՝ փոխանցումը չկատարվի
#
# Փոխանցման ժամանակ գումարը պետք է հանվի ուղարկողից, փոխակերպվի, և ավելացվի ստացողի հաշվին։
#
# Համակարգը պետք է նաև թույլ տա փոփոխել փոխարժեքները և ապահովի, որ դրսից հնարավոր չլինի անմիջապես փոխել balance-ը (encapsulation)։
from datetime import datetime


class Transaction:
    def __init__(self,type_, amount, currency,details=""):
        self.type = type_
        self.amount = amount
        self.currency = currency
        self.details = details
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.type}-- {self.amount} --{self.currency}-- {self.details}...{self.timestamp}"

class Account:
    _exchange_rates = {
        ("USD", "AMD"): 400,
        ("AMD", "USD"): 0.0025,
        ("EUR", "USD"): 1.1,
        ("USD","EUR"): 0.9,
        ("EUR", "AMD"): 500,
        ("AMD", "EUR"): 0.0030,
    }


    def __init__(self,owner,balance, currency):
        self.owner = owner
        self._balance = balance
        self.currency = currency
        self.transactions = []
        self.deposit(balance)

    @property
    def balance(self):
        return self._balance

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount
        self.transactions.append(Transaction("DEPOSIT",amount,self.currency))
    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self._balance:
            raise ValueError("Amount exceeds balance")
        self._balance -= amount
        self.transactions.append(Transaction("WITHDRAW",amount,self.currency))

    @staticmethod
    def validate_currency(currency):
        if not isinstance(currency, str) or len(currency) != 3:
            raise ValueError("Currency must be of type str")

    @classmethod
    def update_rate(cls,from_currency,to_currency,rate):
        cls._exchange_rates[(from_currency, to_currency)] = rate

    def _convert(self,amount,to_currency):
        if self.currency == to_currency:
            return amount
        else:
            key = (self.currency,to_currency)
            if key not in self._exchange_rates:
                raise ValueError(f"Currency {to_currency} is not available")
            return amount * self._exchange_rates[key]

    def transfer(self,other_account, amount):
        if self is other_account:
            raise ValueError("Cannot transfer to the same account")

        self.withdraw(amount)
        converted = self._convert(amount,other_account.currency)
        other_account._balance += converted
        self.transactions.append(Transaction("TRANSFER_OUT",amount, self.currency,f"to {other_account.owner}"))
        other_account.transactions.append(Transaction("TRANSFER_IN",converted, other_account.currency,f"from {self.owner}"))


    def show_transactions(self):
        for t in self.transactions:
            print(t)


a = Account("Hovhannes",1000,"USD")
b = Account("Anahit",2000,"EUR")
c = Account("John",100000,"AMD")

a.transfer(b,500)
print(a.balance)
print(b.balance)
print(b.show_transactions())

