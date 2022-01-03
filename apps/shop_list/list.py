from django.conf import settings

from apps.product.models import Product
from django.contrib.auth.decorators import login_required


class List(object):
    
    def __init__(self, request):
        self.session = request.session
        list = self.session.get(settings.LIST_SESSION_ID)

        if not list:
            list= self.session[settings.LIST_SESSION_ID] = {}
        
        self.list = list

    def __iter__(self):
        for p in self.list.keys():
            self.list[str(p)]['product'] = Product.objects.get(pk=p)
        
        for item in self.list.values():
            item['total_price'] = item['product'].price * item['quantity']

            yield item
    
    def __len__(self):
        return sum(item['quantity'] for item in self.list.values())
    
    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)
        
        if product_id not in self.list:
            self.list[product_id] = {'quantity': 1, 'id': product_id}
        
        if update_quantity:
            self.list[product_id]['quantity'] += int(quantity)

            if self.list[product_id]['quantity'] == 0:
                self.remove(product_id)
                        
        self.save()
    
    def remove(self, product_id):
        if product_id in self.list:
            del self.list[product_id]
            self.save()

    def save(self):
        self.session[settings.LIST_SESSION_ID] = self.list
        self.session.modified = True
    
    def clear(self):
        del self.session[settings.LIST_SESSION_ID]
        self.session.modified = True
    
    def get_total_cost(self):
        for p in self.list.keys():
            self.list[str(p)]['product'] = Product.objects.get(pk=p)

        return sum(item['quantity'] * item['product'].price for item in self.list.values())