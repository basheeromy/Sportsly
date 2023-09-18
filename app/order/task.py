"""
Tasks from order app.
"""

from app.celery import app

@app.task
def send_order_details(
    product,
    quantity,
    shipping_address,
    billing_address,
    user
):
    print(
        f"user is {user}, "
        f"shipping address is {shipping_address}, "
        f"billing address is {billing_address}, "
        f"product is {product}, "
        f"quantity is {quantity}"
        )
