from django.db import models
from PIL import Image

from users.models import Profile

class Rent (models.Model):
    title           = models.CharField(max_length=50)
    long_rent       = models.FloatField()
    short_rent      = models.FloatField()
    category        = models.CharField(max_length=50)
    accessory_1     = models.CharField(max_length=25, null=True)
    accessory_2     = models.CharField(max_length=25, null=True)
    accessory_3     = models.CharField(max_length=25, null=True)
    accessory_4     = models.CharField(max_length=25, null=True)
    accessory_5     = models.CharField(max_length=25, null=True)
    image           = models.ImageField(default='default.jpg', upload_to='rent_pics')
    present_Value   = models.FloatField(default=2500)


    def __str__(self):
        return self.title

"""
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
"""
class Order(models.Model):
	customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	"""@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping"""

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total  

class OrderItem(models.Model):
	product = models.ForeignKey(Rent, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.short_rent * self.quantity * self.quantity
		return total 


class ShippingAddress(models.Model):
	customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address