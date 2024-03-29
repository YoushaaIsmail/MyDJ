from django.conf import settings
from decimal import Decimal
from .models import Product,Order
class Cart(object):

    def __init__(self,request):
        self.session=request.session
        cart =self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart=self.session[settings.CART_SESSION_ID]={}
        self.cart=cart    

    def add(self,product,quantity=1,override_quantity=False):
        product_id=str(product.id)
        if product_id not in self.cart:
            self.cart[product_id]={'quantity':0,'price':str(product.name_prod.PRDPrice)}

        if override_quantity:
            self.cart[product_id]['quantity']=quantity        
        else:
            self.cart[product_id]['quantity']+=quantity    
        self.save()

    def save(self):
        self.session.modified= True        

    def remove(self,Product):
        product_id=str(Product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        print(product_ids)
        pro = Order.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in pro:
          cart[str(product.id)]['product'] = product
        for item in cart.values():
           item['price'] = item['price'].replace(',', '.')
           print( item['price'])
           item['total_price'] = item['price'] * item['quantity']
           yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    def get_total_price(self):
         return (sum(Decimal(item['price'].replace(',', '.')) * item['quantity'] for item in self.cart.values()))+3

    def clean(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()    
