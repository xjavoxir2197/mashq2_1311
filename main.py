class BankAccount:
    """
    Asosiy Bank hisobi klassi.
    Hisob raqami, mijoz ismi va balansni boshqaradi.
    """
    def __init__(self, account_number, customer_name, initial_balance=0):
        # Maxfiy (private) atributlar:
        self.__account_number = account_number
        self.__customer_name = customer_name
        
        # Balans manfiy bo'lmasligi uchun tekshirish
        if initial_balance < 0:
            raise ValueError("Boshlang'ich balans manfiy bo'lishi mumkin emas.")
        self.__balance = initial_balance
        print(f"Hisob ochildi: {self.__customer_name}, №{self.__account_number}. Boshlang'ich balans: {self.__balance} so'm.")

    def deposit(self, amount):
        """
        Hisobga pul kiritish (qo'yish).
        """
        if amount > 0:
            self.__balance += amount
            print(f"{amount} so'm kiritildi. Yangi balans: {self.__balance} so'm.")
        else:
            print("Xatolik: Kiritiladigan summa musbat bo'lishi kerak.")

    def withdraw(self, amount):
        """
        Hisobdan pul yechish.
        Cheklov: Balans manfiy bo'lishi mumkin emas.
        """
        if amount > 0:
            if self.__balance - amount >= 0:
                self.__balance -= amount
                print(f"{amount} so'm yechildi. Yangi balans: {self.__balance} so'm.")
            else:
                print(f"Xatolik: Balans yetarli emas. Joriy balans: {self.__balance} so'm.")
        else:
            print("Xatolik: Yechiladigan summa musbat bo'lishi kerak.")

    def get_balance(self):
        """
        Balans qiymatini faqat o'qish (qaytarish) uchun metod.
        """
        return self.__balance

    def get_info(self):
        """
        Hisob haqida umumiy ma'lumotni qaytaradi (Tekshirish uchun).
        """
        return (f"Hisob raqami: {self.__account_number}, "
                f"Mijoz: {self.__customer_name}, "
                f"Balans: {self.__balance} so'm")


class PremiumAccount(BankAccount):
    """
    BankAccount klassidan meros olgan Premium hisob.
    Chegirmali foiz stavkasi bilan ishlaydi.
    """
    def __init__(self, account_number, customer_name, initial_balance=0, interest_rate=0.01):
        # Ota klassning konstruktorini chaqirish
        super().__init__(account_number, customer_name, initial_balance)
        
        # Premium hisobga xos chegirmali foiz stavkasi (masalan, 1%)
        self.__interest_rate = interest_rate
        print(f"(Premium Hisob) Foiz stavkasi: {self.__interest_rate * 100:.1f}%")

    def apply_interest(self):
        """
        Hisobga foiz stavkasini qo'llaydi.
        """
        # Balansga to'g'ridan-to'g'ri emas, ota klassning metodlari orqali kirish
        current_balance = self.get_balance()
        interest_amount = current_balance * self.__interest_rate
        
        # deposit() metodidan foydalanib balansni yangilash
        self.deposit(interest_amount)
        print(f"Premium foiz hisoblandi: {interest_amount:.2f} so'm.")

    def get_interest_rate(self):
        """
        Foiz stavkasini faqat o'qish uchun metod.
        """
        return self.__interest_rate


# --- Kodni sinab ko'rish ---

print("--- 1. Asosiy BankAccount sinovi ---")
account1 = BankAccount("001", "Alijon Valiyev", 500)

account1.deposit(200)       # Pul kiritish
account1.withdraw(150)      # Pul yechish

# Balansni tekshirish (faqat o'qish)
print(f"Alijonning joriy balansi: {account1.get_balance()} so'm")

# Manfiy balans cheklovini sinash
account1.withdraw(600)      # Balans yetarli emas (Joriy balans 550 so'm)
account1.withdraw(550)      # Pul yechish (Balans 0 bo'ladi)

print("\n--- 2. PremiumAccount sinovi (Meros) ---")
premium_acc = PremiumAccount("002", "Zuhra Karimova", 1000, 0.05) # 5% foiz stavkasi

premium_acc.deposit(500)

# Premium funksiyani sinash
premium_acc.apply_interest()

# Yakuniy balans
print(f"Zuhra Karimova yakuniy balansi: {premium_acc.get_balance():.2f} so'm")
print(premium_acc.get_info())
