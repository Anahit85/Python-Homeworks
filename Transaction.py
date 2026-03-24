from datetime import datetime  # Import für Zeitstempel

"""Dieses Projekt ist ein Multi-Currency Bank System, wo Users unterschiedliche Accounts haben können, zum Beispiel in USD, EUR oder AMD.
Also basically, jeder User hat sein eigenes Konto mit Balance und Currency.
Das System trackt alle Transactions — also deposit, withdraw und transfer — damit man immer History sehen kann.
Wichtig ist, dass Balance niemals negativ werden darf, sonst gibt es einen Error.
Wenn man Geld zwischen Accounts schickt und die Währungen sind verschieden, dann passiert automatisch eine Conversion mit predefined exchange rates.
Wenn kein exchange rate existiert → Transfer wird einfach nicht gemacht (error handling).
Beim Transfer:
.Geld wird vom Sender abgezogen
.dann konvertiert
.und beim Receiver addiert
Außerdem kann man die exchange rates updaten, aber Balance ist protected (encapsulation), das heißt man kann es nicht direkt von außen ändern."""

# Klasse für jede einzelne Transaktion
class Transaction:
    def __init__(self, type_, amount, currency, details=""):
        self.type = type_            # Typ der Transaktion (DEPOSIT, WITHDRAW, etc.)
        self.amount = amount        # Betrag der Transaktion
        self.currency = currency    # Währung (USD, EUR, AMD)
        self.details = details      # Zusatzinfo (z.B. "to John")
        self.timestamp = datetime.now()  # Zeitpunkt der Transaktion

    def __str__(self):
        # Wie die Transaktion als Text dargestellt wird
        return f"{self.type}-- {self.amount} --{self.currency}-- {self.details}...{self.timestamp}"


# Klasse für ein Bankkonto
class Account:
    # Wechselkurse zwischen Währungen (Klassenvariable)
    _exchange_rates = {
        ("USD", "AMD"): 400,
        ("AMD", "USD"): 0.0025,
        ("EUR", "USD"): 1.1,
        ("USD","EUR"): 0.9,
        ("EUR", "AMD"): 500,
        ("AMD", "EUR"): 0.0030,
    }

    def __init__(self, owner, balance, currency):
        self.owner = owner              # Name des Besitzers
        self._balance = balance         # Kontostand (privat)
        self.currency = currency        # Währung des Kontos
        self.transactions = []          # Liste aller Transaktionen
        self.deposit(balance)           # Anfangseinzahlung wird gespeichert

    @property
    def balance(self):
        # Getter für den Kontostand (read-only Zugriff)
        return self._balance

    def deposit(self, amount):
        # Geld einzahlen
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount
        self.transactions.append(Transaction("DEPOSIT", amount, self.currency))

    def withdraw(self, amount):
        # Geld abheben
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self._balance:
            raise ValueError("Amount exceeds balance")
        self._balance -= amount
        self.transactions.append(Transaction("WITHDRAW", amount, self.currency))

    @staticmethod
    def validate_currency(currency):
        # Prüft ob Währung korrekt ist (3 Zeichen)
        if not isinstance(currency, str) or len(currency) != 3:
            raise ValueError("Currency must be of type str")

    @classmethod
    def update_rate(cls, from_currency, to_currency, rate):
        # Aktualisiert Wechselkurs für alle Konten
        cls._exchange_rates[(from_currency, to_currency)] = rate

    def _convert(self, amount, to_currency):
        # Interne Methode zur Umrechnung von Währungen
        if self.currency == to_currency:
            return amount
        else:
            key = (self.currency, to_currency)
            if key not in self._exchange_rates:
                raise ValueError(f"Currency {to_currency} is not available")
            return amount * self._exchange_rates[key]

    def transfer(self, other_account, amount):
        # Überweisung zu einem anderen Konto
        if self is other_account:
            raise ValueError("Cannot transfer to the same account")

        self.withdraw(amount)  # Geld vom eigenen Konto abziehen
        converted = self._convert(amount, other_account.currency)  # ggf. umrechnen

        other_account._balance += converted  # Geld beim Empfänger hinzufügen

        # Transaktionen speichern
        self.transactions.append(
            Transaction("TRANSFER_OUT", amount, self.currency, f"to {other_account.owner}")
        )
        other_account.transactions.append(
            Transaction("TRANSFER_IN", converted, other_account.currency, f"from {self.owner}")
        )

    def show_transactions(self):
        # Alle Transaktionen anzeigen
        for t in self.transactions:
            print(t)


# ----------- TEST / ANWENDUNG -----------

a = Account("Hovhannes", 1000, "USD")
b = Account("Anahit", 2000, "EUR")
c = Account("John", 100000, "AMD")

# Überweisung von a nach b
a.transfer(b, 500)

# Kontostände anzeigen
print(a.balance)
print(b.balance)

# Transaktionen anzeigen
print(b.show_transactions())