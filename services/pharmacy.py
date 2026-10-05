
from models.medicine import Medicine
from models.order import Order
from models.user import User
from models.customer import Customer
from services.db_connection import DBConnection


class Pharmacy:

    def __init__(self):
        self.db = DBConnection()

    # =========================================================
    # USER / STAFF / ADMIN
    # =========================================================

    def add_new_user(self, username, password_hash, role="staff", status=True):
        """
        System login user 

        Example:
        pharmacy.add_new_user(
            "admin",
            "hashed_password",
            "admin"
        )
        """

        self.db.add_user(
            username,
            password_hash,
            role,
            status
        )

        print("✅ New system user added.")

    def show_all_users(self):
        """
        All system users return
        """

        users = self.db.fetch_users()

        user_objects = []

        for u in users:
            user = User(
                u[0],  # id
                u[1],  # username
                u[2],  # password_hash
                u[3],  # role
                u[4]   # status
            )

            user_objects.append(user)

        return user_objects



    # =========================================================
    # CUSTOMER
    # =========================================================

    def add_new_customer(
        self,
        name,
        phone,
        email=None,
        address=None,
        status=True
    ):
        """
        Make a Customer by Pharmacy
        """

        self.db.add_customer(
            name,
            phone,
            email,
            address,
            status
        )

        print("✅ New customer added.")

    def show_all_customers(self):
            """
            All system customers return
            """
    
            customers = self.db.fetch_customers()
    
            customers_objects = []
    
            for c in customers:
                customer = Customer(
                    c[0],  # id
                    c[1],  # username
                    c[2],  # password_hash
                    c[3],  # role
                    c[4]   # status
                )
    
                customers_objects.append(customer)
    
            return customers_objects

    def get_customer(self, customer_id):
        """
        Fixed customer return
        """

        return self.db.fetch_customer(customer_id)


    # =========================================================
    # MEDICINE
    # =========================================================

    def add_new_medicine(
        self,
        name,
        price,
        stock,
        status=True
    ):
        """
        Make a New medicine
        """

        self.db.add_medicine(
            name,
            price,
            stock,
            status
        )

        print("✅ New medicine added.")

    def show_all_medicines(self):
        """
        All medicines object  return 
        """

        meds = self.db.fetch_medicines()

        med_objects = []

        for m in meds:
            medicine = Medicine(
                m[0],  # id
                m[1],  # name
                m[2],  # price
                m[3],  # stock
                m[4]   # status
            )

            med_objects.append(medicine)

        return med_objects

    def show_all_medicines_old(self):
        """
        Console/debug 
        """

        medicines = self.db.fetch_medicines()

        for m in medicines:
            medicine = Medicine(
                m[0],
                m[1],
                m[2],
                m[3],
                m[4]
            )

            medicine.show_info()


    # =========================================================
    # ORDERS
    # =========================================================

    def place_order(
        self,
        user_id,
        customer_id,
        medicine_id,
        quantity
    ):

        result = self.db.place_order(
            user_id,
            customer_id,
            medicine_id,
            quantity
        )

        print(result)

        return result


    def show_all_orders(self, user_id):
        """
        All orders return
        """

        orders = self.db.fetch_orders(user_id)

        order_objects = []

        for o in orders:

            order = Order(
                o[0],  # id
                o[1],  # user_id
                o[2],  # customer_id
                o[3],  # medicine_id
                o[4],  # quantity
                o[5]   # total_price
            )

            order_objects.append(order)

        return order_objects


    # =========================================================
    # SALES REPORT
    # =========================================================

    def show_sales_report(self):

        report = self.db.sales_report()

        print("\n📊 Sales Report")

        print(
            f"Total Orders: "
            f"{report['total_orders']}"
        )

        print(
            f"Total Sales: "
            f"{report['total_sales']} BDT"
        )

        if report['top_medicine']:

            print(
                f"Top Medicine: "
                f"{report['top_medicine'][0]} "
                f"(Qty: {report['top_medicine'][1]})"
            )

        else:
            print("No sales data yet.")


    # =========================================================
    # CUSTOMER REPORT
    # =========================================================

    def show_customer_report(self, customer_id):

        report = self.db.customer_report(customer_id)

        print("\n📊 Customer Report")

        print(
            f"Customer ID: {customer_id}"
        )

        print(
            f"Total Orders: "
            f"{report['total_orders']}"
        )

        print(
            f"Total Spent: "
            f"{report['total_spent']} BDT"
        )

        if report['medicines']:

            print("\n🧾 Medicines Purchased:")

            for medicine in report['medicines']:

                print(
                    f"- {medicine[0]} "
                    f"(Qty: {medicine[1]})"
                )

        else:

            print("No purchases yet.")

