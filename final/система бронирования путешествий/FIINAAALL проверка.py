print('Все места по 7000 рублей, кроме аварийных 30A и 30F, которые стоят 8000 рублей.')

name = input("Введите ваше полное имя: ")
data = input("Введите ваши контактные данные: ")


print("Выбор места:")
seat_plane = ("""
    ---            1D  1E  1F
    2A  2B  2C     2D  2E  2F
    3A  3B  3C     3D  3E  3F    
    4A  4B  4C     4D  4E  4F
    5A  5B  5C     5D  5E  5F    
    6A  6B  6C     6D  6E  6F
    7A  7B  7C     7D  7E  7F    
    8A  8B  8C     8D  8E  8F
    9A  9B  9C     9D  9E  9F    
    10A 10B 10C    10D 10E 10F
    11A 11B 11C    11D 11E 11F    
    12A 12B 12C    12D 12E 12F
    13A 13B 13C    13D 13E 13F    
    14A 14B 14C    14D 14E 14F
    15A 15B 15C    15D 15E 15F    
    16A 16B 16C    16D 16E 16F
    17A 17B 17C    17D 17E 17F    
    18A 18B 18C    18D 18E 18F
    19A 19B 19C    19D 19E 19F    
    20A 20B 20C    20D 20E 20F
    ---            21D 21E 21F    
    ---            ... ...
    30A 30B 30C    30D 30E 30F
    ---            ... ...
    45A 45B 45C    45D 45E 45F
    """)

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

print(seat_plane)

available_seats = ['1D', '1E', '1F', '2A', '2B', '2C', '2D', '2E', '2F', '3A', '3B', '3C', '3D', '3E', '3F', '4A', '4B',
                   '4C', '4D', '4E', '4F', '5A', '5B', '5C', '5D', '5E', '5F', '6A', '6B', '6C', '6D', '6E', '6F', '7A',
                   '7B', '7C', '7D', '7E', '7F', '8A', '8B', '8C', '8D', '8E', '8F', '9A', '9B', '9C', '9D', '9E', '9F',
                   '10A', '10B', '10C', '10D', '10E', '10F', '11A', '11B', '11C', '11D', '11E', '11F', '12A', '12B',
                   '12C', '12D', '12E', '12F', '13A', '13B', '13C', '13D', '13E', '13F', '14A', '14B', '14C', '14D',
                   '14E', '14F', '15A', '15B', '15C', '15D', '15E', '15F', '16A', '16B', '16C', '16D', '16E', '16F',
                   '17A', '17B', '17C', '17D', '17E', '17F', '18A', '18B', '18C', '18D', '18E', '18F', '19A', '19B',
                   '19C', '19D', '19E', '19F', '20A', '20B', '20C', '20D', '20E', '20F', '21D', '21E', '21F', '30A',
                   '30B', '30C', '30D', '30E', '30F', '45A', '45B', '45C', '45D', '45E', '45F']

place = input('Какое место вы хотите выбрать? ')

if place in available_seats:
    if place in ['30A', '30F']:
        price = 8000
        print(f'Вы выбрали место {place}, стоимость билета составляет {price} рублей.')
    else:
        price = 7000
        print(f'Вы выбрали место {place}, стоимость билета составляет {price} рублей.')
else:
    print(f'Место {place} недоступно. Пожалуйста, выберите другое место.')

trip = Tour("Приложение 228", "21E", "Москва")

trip.check_out()

trip.check_out()

