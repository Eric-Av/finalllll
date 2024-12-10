class Tour:
    def __init__(self, flight_search, booking_tickers, routes):
        self.flight_search = flight_search
        self.booking_tickers = booking_tickers
        self.routes = routes
        self.checked_out = False

    def flight_search(self):
        print(f'Рейс: {self.flight_search}')

    def booking_tickers(self):
        print(f'Бронь билетов: {self.booking_tickers}')

    def routes(self):
        print(f'Управлние билетами: {self.routes}')

    def check_out(self):
        if self.checked_out:
            print("Билет выдан пользователю")
        else:
            self.checked_out = True
            print("Выдаем билет пользователю")

    def check_in(self):
        if not self.checked_out:
            print("Есть билет")
        else:
            self.checked_out = False
            print("Возврат билета")
    
# создаем объект книги
trip = Tour("Приложение 228", "21E", "Москва")

# выдаем книгу, проверяем статус
trip.check_out()

# проверяем статус повторно
trip.check_out()

# принимаем книгу от читателя
trip.check_in()

# проверяем статус книги повторно
trip.check_in()    