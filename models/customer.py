
class Customer:

    def __init__(
        self,
        customer_id,
        name,
        phone,
        email,
        address,
        status
    ):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.status = status

    def show_info(self):
        print(
            f"ID: {self.customer_id}, "
            f"Name: {self.name}, "
            f"Phone: {self.phone}, "
            f"Email: {self.email}, "
            f"Address: {self.address}, "
            f"Status: {self.status}"
        )

