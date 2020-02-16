import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        total = 0
        now = dt.datetime.now().date()
        return sum([record.amount for record in self.records if record.date == now])

    def get_week_stats(self):
        total = 0 
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
        curr_dict = { 'rub': ['руб', 1, self.RUB_RATE], 'usd': ['USD', 2, self.USD_RATE], 'eur': ['Euro', 2, self.EURO_RATE]}
        for curr in curr_dict.keys():
            if currency == curr:
                total /= curr_dict[curr][2]
                curr_limit /= curr_dict[curr][2]
                if curr_limit > total:
                    return f'На сегодня осталось {round(curr_limit - total, curr_dict[curr][1])} {curr_dict[curr][0]}'
                elif curr_limit == total:
                    return f'Денег нет, держись'
                else:
                    return f'Денег нет, держись: твой долг - {round(total - curr_limit, curr_dict[curr][1])} {curr_dict[curr][0]}'

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        total = super().get_today_stats()
        day_limit = self.limit - total
        if day_limit > 0 :
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {day_limit} кКал'
        else:
            return 'Хватит есть!'
