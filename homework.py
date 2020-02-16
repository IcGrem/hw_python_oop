import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        now = dt.datetime.now().date()
        return sum([record.amount for record in self.records if record.date == now])

    def get_week_stats(self):
        now = dt.datetime.now().date()
        last_seven = now - dt.timedelta(days=7)
        return sum([record.amount for record in self.records if now >= record.date >= last_seven])

class Record:
    def __init__(self, amount, comment, date = None):
        print(date)
        self.amount = amount
        self.comment = comment
        if date == None:
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

class CashCalculator(Calculator):
    USD_RATE = 60.5
    EURO_RATE = 70.5
    RUB_RATE = 1
    def get_today_cash_remained(self, currency='rub'):
        total = super().get_today_stats()
        curr_limit = self.limit
        curr_dct = { 'rub': ('руб', 1, self.RUB_RATE), 'usd': ('USD', 2, self.USD_RATE), 'eur': ('Euro', 2, self.EURO_RATE)}
        if currency in curr_dct:
            curr_name, curr_round, curr_rate = curr_dct[currency]
            total /= curr_rate
            curr_limit /= curr_rate
            if curr_limit > total:
                bill = round(curr_limit - total, curr_round)
                return f'На сегодня осталось {bill} {curr_name}'
            elif curr_limit == total:
                return f'Денег нет, держись'
            else:
                debt = round(total - curr_limit, curr_round)
                return f'Денег нет, держись: твой долг - {debt} {curr_name}'

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        total = super().get_today_stats()
        day_limit = self.limit - total
        if day_limit > 0 :
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {day_limit} кКал'
        return 'Хватит есть!'
