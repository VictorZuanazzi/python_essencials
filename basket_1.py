class basket (object):
    '''A basket to contain items.

    Attributes:
        name: name of the basket.
        price: price of the basket.
        owner: name of the owner of the basket.
        volume: a float representing the total volume of the basket.
        free_volume: a float representing the volume left in the basket.
        items: a list of list of str and float and float items in the basket, their volume and their price.


    '''
    def __init__(self, name, owner, volume, items):
        '''Return a basket object whose:
        name is *name* - str;
        price is *price* - number;
        owner is *owner* - str;
        volume is *volume* - number;
        which the volume still available is *free_volume* - number
        and which items name, volume and price are the list items [[str, number, number],...].
        '''

        self.name = name
        self.owner = owner
        self.volume= volume
        self.items = items

        self.free_volume = self.free_volume_calc(items)
        self.price = self.basket_price(items)

    def free_volume_calc(self, items):
        '''Return the available volume of the basket used by the *items*
        '''
        
        return self.volume - self.total_volume_calc(items)

    def total_volume_calc(self, items):
        '''Return the used volume of the basket used by the *items*
        '''
        
        used_volume = 0
        for i in range(len(items)):
            used_volume = used_volume + items[i][1]
        return used_volume

    def basket_price(self, items):
        '''Return the price of the basket by summing the price of the *items*.
        '''
        
        total_price = 0
        for i in range(len(items)):
            total_price += items[i][2]
        return total_price
    

    def add_items(self, new_items):
        '''Adds the list *new_items* to the basket.
           It also update the price and the free_volume of the basket.
        '''
        if self.total_volume_calc(self.items) < self.free_volume:
            for i in new_items:
                self.items.append(i)
                self.free_volume = self.free_volume_calc(self.items)
                self.price = self.basket_price(self.items)
                
    


        

        

    
        
    
