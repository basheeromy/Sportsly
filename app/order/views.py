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
from user.models import (
    Address,
    BillingAddress
)
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
        "handle order placement."
        
        try:
            products = request.data.get('products').split(',')
            quantity = json.loads(request.data.get('quantity'))
            shipping_address = Address.objects.get(
                id=int(request.data.get('shipping_address'))
            )
            billing_address = BillingAddress.objects.get(
                id=int(request.data.get('billing_address'))
            )
            payment_mode = request.data.get('payment_mode')
            user = request.user

            # Create an order instance from given data.
            order = Order(
                user = user,
                shipping_address = shipping_address,
                billing_address = billing_address,
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
                if product.quantity < product_quantity:
                    message = (
                        f"Available quantity of product {product.name.name} "
                        f"{product.size} {product.color} is only "
                        f"{product.quantity}"
                    )
                    return Response(
                        message,
                        status=status.HTTP_400_BAD_REQUEST)

                product.quantity -= product_quantity
                product.save()
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

        except ValueError as e:
            return Response(
                f"Invalid input, use an integer : {str(e)}",
                status=status.HTTP_400_BAD_REQUEST
            )

        except (Address.DoesNotExist):
            return Response("Invalid Address ID", status=status.HTTP_404_NOT_FOUND)

        except (BillingAddress.DoesNotExist):
            return Response(
                "Invalid Billing Address ID",
                status=status.HTTP_404_NOT_FOUND
            )

        except (Product_item.DoesNotExist):
            return Response("Invalid Product_item ID", status=status.HTTP_404_NOT_FOUND)

        except KeyError as e:
            return Response(
                f"Invalid key in request data: {str(e)}",
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
