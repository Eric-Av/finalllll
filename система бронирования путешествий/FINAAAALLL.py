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
            print("Книга находится у абонента.")
        else:
            self.checked_out = True
            print("Выдаем книгу абоненту.")

    def check_in(self):
        if not self.checked_out:
            print("Книга в наличии.")
        else:
            self.checked_out = False
            print("Принимаем книгу в библиотеку.")
    
# создаем объект книги
book1 = Tour("Война и мир", "Л.Н. Толстой", "978-0743273565")

# выдаем книгу, проверяем статус
book1.check_out()

# проверяем статус повторно
book1.check_out()

# принимаем книгу от читателя
book1.check_in()

# проверяем статус книги повторно
book1.check_in()    