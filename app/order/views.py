"""Views to manage orders"""

import json
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView
)
from rest_framework.response import Response
from .models import (
    Order,
    OrderItem
)
from .serializers import (
    OrderSerializer,
    SpecialSerializer
)
from product.models import (
    Product_item,
)
from user.models import Address
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions


class OrderAndOrderItemListCreateAPIView(ListCreateAPIView):
    """View to create and list orders and order items at once."""

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.prefetch_related('orderitem_set')


    def get_serializer_class(self):
        # choose serializer class based on request method.
        
        if self.request.method == 'POST':
            return SpecialSerializer
        return OrderSerializer


    def create(self, request, *args, **kwargs):

        products = request.data.get('products').split(',')
        quantity = json.loads(request.data.get('quantity'))
        shipping_address = Address.objects.get(
            id=int(request.data.get('shipping_address'))
        )
        payment_mode = request.data.get('payment_mode')
        user = request.user

        # Create an order instance from given data.
        order = Order(
            user = user,
            shipping_address = shipping_address,
            price = 0.00,
            order_status = "Placed",
            payment_mode = payment_mode,
            payment_status = "Not paid and this works."

        )
        # save order instance.
        order.save()

        # Careate order items instances.
        for product in products:

            product_quantity = quantity[product]
            product_id = int(product)

            product = Product_item.objects.select_related(
                "name"
            ).get(id=product_id)
            seller = product.name.seller
            price = product.price * product_quantity

            order_item = OrderItem(
                order = order,
                seller = seller,
                product = product,
                quantity = product_quantity,
                price = price
            )

            # save order item instance.
            order_item.save()

            # edit order instance to update total price.
            order.price += float(price)

            # save order instance with changes.
            order.save()

        """res = json.dumps(
            order,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4
        )"""
        return Response(
            "Order Placed Successfully", status=status.HTTP_201_CREATED
        )
