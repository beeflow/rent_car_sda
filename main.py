"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from typing import List

from models.car import Car
from models.customer import Customer
from models.rentcar import RentCar
from views.car_view import CarView

if __name__ == '__main__':
    # Rent a car ...
    cars: List[Car] = CarView().find()
    car: Car = cars[0]
    user: Customer = Customer().get(licence_id=input('Numer prawa jazdy: '))

    RentCar(car=car, customer=user).save()
    print("Auto wypożyczone")
