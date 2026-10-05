
class Medicine:

    def __init__(
        self,
        medicine_id,
        name,
        price,
        stock,
        status
    ):
        self.medicine_id = medicine_id
        self.name = name
        self.price = price
        self.stock = stock
        self.status = status

    def show_info(self):
        print(
            f"ID: {self.medicine_id}, "
            f"Name: {self.name}, "
            f"Price: {self.price}, "
            f"Stock: {self.stock}, "
            f"Status: {self.status}"
        )

