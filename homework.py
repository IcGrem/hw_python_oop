import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, Record):
        self.record = Record
        self.records.append(self.record)

    def get_today_stats(self):
        total = 0
        now = dt.datetime.now().date()
        return sum ([total + record.amount for record in self.records if record.date == now])

    def get_week_stats(self):
        total = 0 
        now = dt.datetime.now().date()
        last_seven = now - dt.timedelta(days=7)
        return sum ([total + record.amount for record in self.records if now >= record.date >= last_seven])

class Record:
    def __init__(self, amount, comment, date = ''):
        print(date)
        self.amount = amount
        self.comment = comment
        if date == '':
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

class CashCalculator(Calculator):
    USD_RATE = 60.5
    EURO_RATE = 70.5
    def get_today_cash_remained(self, currency='rub'):
        euro = self.EURO_RATE
        usd = self.USD_RATE
        total = super().get_today_stats()
        curr_limit = self.limit
        curr_round = 2
        if currency == 'rub':
            curr_name = 'руб'
            curr_round = 1
            total /= 1
        if currency == 'usd':
            total /= usd
            curr_name = 'USD'
            curr_limit /= usd
            curr_round = 2
        if currency == 'eur':
            total /= euro
            curr_name = 'Euro'
            curr_limit /= euro
            curr_round = 2
        if curr_limit > total:
            return (f'На сегодня осталось {round(curr_limit - total, curr_round)} {curr_name}')
        elif curr_limit == total:
            return (f'Денег нет, держись')
        else:
            return (f'Денег нет, держись: твой долг - {round(total - curr_limit, curr_round)} {curr_name}')

class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        total = super().get_today_stats()
        day_limit = self.limit - total
        if day_limit > 0 :
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {day_limit} кКал') 
        else:
            return ('Хватит есть!')
