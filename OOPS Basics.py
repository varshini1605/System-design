class ShoppingCart(object):
    def __init__(self):
        self.total=0
        self.item={}
    
    def add_item(self, item_name,quantity,price):
        self.total+=(quantity * price)
        self.item.update({item_name : quantity})
        #print(self.total)
    
    def remove_item(self, item_name,quantity,price):
        self.total-=(quantity * price)
        if quantity>self.item[item_name]:
            del self.item[item_name]
        self.item[item_name]-=quantity

    def checkout(self,cash_paid):
        balance=0
        if cash_paid<self.total:
            return "amount to be paid {}".format(self.total-cash_paid)
        
        return "paid"

cart=ShoppingCart()
cart.add_item('A',1,2)
cart.add_item('B', 5, 20)
print(cart.total)
#cart.remove_item('B', 5, 20)
print(cart.total)
print(cart.checkout(600))
