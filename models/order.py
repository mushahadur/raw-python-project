
class Order:

    def __init__(
        self,
        order_id,
        user_id,
        customer_id,
        medicine_id,
        quantity,
        total_price
    ):
        self.order_id = order_id
        self.user_id = user_id
        self.customer_id = customer_id
        self.medicine_id = medicine_id
        self.quantity = quantity
        self.total_price = total_price

    def show_info(self):
        print(
            f"Order ID: {self.order_id}, "
            f"User ID: {self.user_id}, "
            f"Customer ID: {self.customer_id}, "
            f"Medicine ID: {self.medicine_id}, "
            f"Quantity: {self.quantity}, "
            f"Total: {self.total_price}"
        )

