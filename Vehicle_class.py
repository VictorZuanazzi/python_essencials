from abc import ABCMeta, abstractmethod

class Vehicle (object):
    '''A vehicle for sale by Poisonmylunghs Car Dealership.

    Arributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    '''

    __metaclass__ = ABCMeta

    base_sale_price = 0
    wheels = 0

    def __init__(self, wheels, miles, make, model, year, sold_on):
        '''Return a new Vehicle object.'''
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        '''Return the sale price for this vehicle as float amount.
        '''

        if self.sold_on is not None:
            return 0.0 #Not yet sold.
        return 5000*self.wheels


    def purchase_price(self):
        '''Return the price for which we would pay to purchase the vehicle.
        '''
        if self.sold_on is None:
            return 0.0 #Not yet sold.
        return self.base_sales_price -(.10*self.miles)

    @abstractmethod
    def vehicle_type(self):
        '''Return a string representing the type of vehicle this is.
        '''
        pass
    

class Car(Vehicle):
    '''A car for sale by Poisonmylunghs Car Dealership.
    '''
    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        '''Return a string representing the type of vehicle this is.
        '''
        return 'car'

class Truck(Vehicle):
    '''A truck for sale by Poisonmylunghs Car Dealership.
    '''

    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        '''Return a string representing the thype of vehicle this is.
        '''

        return 'truck'


