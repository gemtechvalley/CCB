from django.urls import path
from .import views
from .views import RentListView


urlpatterns = [
    path('', RentListView.as_view(), name='rent-index'),
    #path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="rent-checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	#path('process_order/', views.processOrder, name="process_order"),


]



