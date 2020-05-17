"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from typing import List

from peewee import IntegrityError

from models.brand import Brand
from models.car import Car
from models.carmodel import CarModel
from models.carstatus import CarStatus


class CarView:
    def get(self):
        print("Lista pojazdów")
        print("--------------")

        for car in Car().select():
            print(car.id, car)

    def find(self):
        print("Znajdź pojazd")
        print("-----------------")

        register_number = input('Numer rejestracyjny: ')

        try:
            status = input('(opcja) Status [d] - dostępny, [n] - niedostępny: ')
        except ValueError:
            status = None

        if status:
            cars = Car().select().where(
                (Car.register_number == register_number) &
                (CarStatus.name == ('Dostępny' if status == 'd' else 'Wypożyczony'))
            ).join(CarStatus)
        else:
            cars = Car().select().where(Car.register_number == register_number)

        result: List[Car] = []

        for car in cars:
            result.append(car)
            print(car.id, car, car.status)

        return result

    def post(self):
        print("Dodawanie pojazdu")
        print("-----------------")

        brand = self._get_brand_object(input('Marka: '))
        model = self._get_car_model_object(input('Model: '), brand)
        status = CarStatus().get(name='Dostępny')
        register_number = input('Numer rejestracyjny: ')

        try:
            production_year = int(input('Rok produkcji (opcjonalnie): '))
        except ValueError:
            production_year = None

        try:
            Car(
                brand=brand, model=model, status=status, register_number=register_number,
                production_year=production_year
            ).save()
        except IntegrityError:
            print(f'Pojazd o numerze rejestracyjnym {register_number} już istnieje.')

    @staticmethod
    def _get_brand_object(brand_name: str) -> Brand:
        return Brand().get_or_create(name=brand_name)[0]

    @staticmethod
    def _get_car_model_object(car_model_name: str, brand: Brand) -> CarModel:
        return CarModel().get_or_create(name=car_model_name, brand=brand)[0]
